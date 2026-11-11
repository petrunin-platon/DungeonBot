"""Какие скриншоты нужны руководству и какие уже лежат в guide/images (задача 15, шаг 10.16). Ничего не меняет.

Скриншоты лежат по папкам языков, имя файла — как в тексте руководства (![Подпись](images/имя.png)):
- guide/images/ru/ — для русского руководства;
- guide/images/en/ — для английского и для всех остальных языков, пока у них нет своих (окно берёт:
  папку своего языка → общую guide/images/ → en/ → ru/, ui/guide_renderer.find_image);
- guide/images/ — картинка без надписей, одна на все языки.
Расширение любое из .png, .jpg, .jpeg, .webp: usb_debug.jpg подойдёт вместо usb_debug.png.

Запуск: двойной щелчок по guide_images.bat или в cmd в папке бота — python guide_images.py (можно с языками: python guide_images.py RU EN DE).
"""
import os
import sys

from ui import guide_renderer as gr

GUIDE_DIR = gr.GUIDE_DIR
DEFAULT_LANGS = ("RU", "EN")


def needed_images(text):
    """Картинки из текста руководства по порядку: [(путь из текста, подпись, номер раздела, заголовок раздела)]."""
    guide = gr.parse(text)
    found, seen = [], set()
    for section in guide.all_sections():
        for block in section.blocks:
            if isinstance(block, gr.Image) and block.path not in seen:
                seen.add(block.path)
                found.append((block.path, block.caption, section.number, section.title or "вступление"))
    return found


def image_report(lang, text, folder=GUIDE_DIR):
    """Для языка lang: [(имя файла, подпись, раздел, где нашлась картинка: "own" | "common" | "other" | "")] и лишние файлы
    в папке этого языка (в руководстве их нет)."""
    guide_path = os.path.join(folder, f"{lang.lower()}.md")
    own = os.path.join(folder, "images", lang.lower())
    common = os.path.join(folder, "images")
    rows = []
    for path, caption, number, title in needed_images(text):
        found = gr.find_image(guide_path, path)
        where = ""
        if found:
            place = os.path.normcase(os.path.normpath(os.path.dirname(found)))
            where = ("own" if place == os.path.normcase(os.path.normpath(own))
                     else "common" if place == os.path.normcase(os.path.normpath(common)) else "other")
        rows.append((os.path.basename(path), caption, f"{number}. {title}", where, found))
    wanted = {os.path.splitext(os.path.basename(p))[0].lower() for p, *_ in needed_images(text)}
    try:
        extra = sorted(name for name in os.listdir(own)
                       if name.lower().endswith(gr.IMAGE_EXTS) and os.path.splitext(name)[0].lower() not in wanted)
    except OSError:
        extra = []
    return rows, extra


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    langs = [code.upper() for code in (argv if argv is not None else sys.argv[1:])] or list(DEFAULT_LANGS)
    _, text = gr.read_guide("RU", GUIDE_DIR)
    if not text:
        print(f"[КАРТИНКИ] Нет файла {GUIDE_DIR}/ru.md. Запускай из папки бота.")
        return 1
    for lang in langs:
        rows, extra = image_report(lang, text)
        ready = sum(1 for row in rows if row[3] in ("own", "common"))
        own = f"{GUIDE_DIR}/images/{lang.lower()}/"
        print(f"\n[КАРТИНКИ] {lang}: готово {ready} из {len(rows)}. Папка: {own}")
        for name, caption, section, where, found in rows:
            if where == "own":
                print(f"  есть   {name}")
            elif where == "common":
                print(f"  есть   {name}  (общая: {GUIDE_DIR}/images/)")
            else:
                note = f"  — пока берётся {os.path.relpath(found, GUIDE_DIR)}" if found else ""
                print(f"  НЕТ    {name}{note}\n         раздел {section}: {caption}")
        for name in extra:
            print(f"  лишний {name}  (в руководстве такой картинки нет — проверь имя файла)")
    print("\n[КАРТИНКИ] Новый скриншот — в папку своего языка, имя — как в списке. Окно покажет его при следующем "
          "открытии «Руководства».")
    return 0


if __name__ == "__main__":
    sys.exit(main())
