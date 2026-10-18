"""Minimalny generator specyfikacji DOCX oparty wyłącznie na bibliotece standardowej."""

import argparse
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", WORD_NS)

def wtag(name: str) -> str:
    return f"{{{WORD_NS}}}{name}"


def add_text(parent: ET.Element, text: str, *, bold: bool = False, size: int | None = None) -> None:
    run = ET.SubElement(parent, wtag("r"))
    if bold or size:
        props = ET.SubElement(run, wtag("rPr"))
        if bold:
            ET.SubElement(props, wtag("b"))
        if size:
            ET.SubElement(props, wtag("sz")).set(wtag("val"), str(size))
    ET.SubElement(run, wtag("t")).text = text


def paragraph(parent: ET.Element, text: str, *, bold: bool = False, size: int | None = None) -> None:
    add_text(ET.SubElement(parent, wtag("p")), text, bold=bold, size=size)


def cell_text(cell: ET.Element, text: str, *, bold: bool = False) -> None:
    paragraph(cell, text, bold=bold)


def build_document(product: dict) -> bytes:
    document = ET.Element(wtag("document"))
    body = ET.SubElement(document, wtag("body"))
    paragraph(body, product.get("product_name", "Specyfikacja produktu"), bold=True, size=32)
    identity = []
    for label, key in (("Producent", "manufacturer"), ("Numer katalogowy", "catalog_number")):
        if product.get(key):
            identity.append(f"{label}: {product[key]}")
    if identity:
        paragraph(body, "   |   ".join(identity), bold=True)
    if product.get("category"):
        paragraph(body, f"Kategoria: {product['category']}")
    if product.get("variant"):
        paragraph(body, f"Wariant: {product['variant']}")
    if product.get("ean", {}).get("value"):
        paragraph(body, f"EAN: {product['ean']['value']}")
    paragraph(body, f"Status walidacji: {product['validation_status']}", bold=True)
    paragraph(body, "Dane techniczne", bold=True, size=26)

    table = ET.SubElement(body, wtag("tbl"))
    props = ET.SubElement(table, wtag("tblPr"))
    borders = ET.SubElement(props, wtag("tblBorders"))
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        ET.SubElement(borders, wtag(edge), {wtag("val"): "single", wtag("sz"): "4", wtag("color"): "B7C9D6"})
    grid = ET.SubElement(table, wtag("tblGrid"))
    for width in (3000, 3000, 3360):
        ET.SubElement(grid, wtag("gridCol")).set(wtag("w"), str(width))

    header = ET.SubElement(table, wtag("tr"))
    for text in ("Parametr", "Wartość", "Źródło / lokalizacja dowodu"):
        cell_text(ET.SubElement(header, wtag("tc")), text, bold=True)

    current_group = None
    for key, parameter in product.get("parameters", {}).items():
        group = parameter.get("group")
        if group and group != current_group:
            group_row = ET.SubElement(table, wtag("tr"))
            group_cell = ET.SubElement(group_row, wtag("tc"))
            cell_text(group_cell, group, bold=True)
            for _ in range(2):
                ET.SubElement(group_row, wtag("tc"))
            current_group = group
        row = ET.SubElement(table, wtag("tr"))
        value = parameter.get("value", "")
        unit = parameter.get("unit")
        if unit:
            value = f"{value} {unit}"
        fields = (
            parameter.get("label", key.replace("_", " ").capitalize()),
            str(value),
            f"{parameter.get('source', '')}: {parameter.get('evidence', '')}",
        )
        for text in fields:
            cell_text(ET.SubElement(row, wtag("tc")), text)

    sources = product.get("sources", [])
    if sources:
        paragraph(body, "Źródła danych", bold=True, size=24)
        for source in sources:
            title = source.get("title", source.get("source_id", "Źródło"))
            url = source.get("url")
            accessed = source.get("accessed_on")
            details = [title]
            if url:
                details.append(url)
            if accessed:
                details.append(f"dostęp: {accessed}")
            paragraph(body, " — ".join(details))
    section = ET.SubElement(body, wtag("sectPr"))
    ET.SubElement(section, wtag("pgSz"), {wtag("w"): "11906", wtag("h"): "16838"})
    ET.SubElement(section, wtag("pgMar"), {wtag("top"): "850", wtag("right"): "850", wtag("bottom"): "850", wtag("left"): "850", wtag("header"): "425", wtag("footer"): "425", wtag("gutter"): "0"})
    return ET.tostring(document, encoding="utf-8", xml_declaration=True)


def generate_docx(data_path: Path, output_path: Path) -> None:
    product = json.loads(data_path.read_text(encoding="utf-8"))
    if product.get("validation_status") != "PASS":
        raise ValueError("Generowanie wstrzymane: status walidacji musi wynosić PASS")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''
    relationships = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", relationships)
        docx.writestr("word/document.xml", build_document(product))


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Generuje DOCX ze zwalidowanego rekordu produktu.")
    parser.add_argument("data", type=Path, help="Ścieżka do JSON produktu ze statusem PASS")
    parser.add_argument("--output", type=Path, help="Ścieżka wyjściowa; domyślnie output/<nazwa-rekordu>.docx")
    args = parser.parse_args()
    output_path = args.output or (repo / "output" / f"{args.data.stem}.docx")
    generate_docx(args.data, output_path)
    print(f"Zapisano: {output_path}")


if __name__ == "__main__":
    main()
