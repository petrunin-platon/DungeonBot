# sos_answers.py
# Разбор ответа на окна SOS (задача 18, шаг 4). Раньше main.py разбирал ответ цепочкой if/elif в трёх местах,
# и непонятный ответ проходил молча: в окне «Требуется вмешательство» бот жал «ОК» и не засчитывал комнату,
# в «Нет подходящего пака» пытался поставить пак ["STOP"] и выключался, NEW_PACK без двоеточия ронял бота.
# Теперь каждое окно принимает только свои команды; на любую другую бот пишет строку и спрашивает ещё раз.
# Без OpenCV и игры — проверяется тестами (tests/test_sos_answers.py).

# Окна, которые бот открывает строкой [SOS_TRIGGER]
SOS = "sos"            # «Требуется вмешательство» (плохой бой)
TEST = "test"          # «Пак справился» (TEST_SUCCESS)
NO_TEAM = "no_team"    # «Нет подходящего пака» (NO_VALID_TEAM)

WINDOW_NAMES = {SOS: "«Требуется вмешательство»", TEST: "«Пак справился»", NO_TEAM: "«Нет подходящего пака»"}

# Какие команды понимает каждое окно (как их шлют окно программы и Telegram, CLAUDE.md, «Связь GUI и бота»)
ALLOWED = {
    SOS: ("MANUAL", "STOP", "IGNORE", "ROLLBACK"),
    TEST: ("CONFIRM", "ROLLBACK"),
    NO_TEAM: ("MANUAL", "STOP", "NEW_PACK"),
}


class Answer:
    """Понятый ответ. command — MANUAL, STOP, IGNORE, ROLLBACK, CONFIRM или NEW_PACK;
    team — пак из ответа (ROLLBACK:..., NEW_PACK:...) или None; source — "telegram" для ROLLBACK_TG, иначе "gui"."""

    def __init__(self, command, team=None, source="gui"):
        self.command, self.team, self.source = command, team, source

    def __repr__(self):
        return f"Answer({self.command!r}, {self.team!r}, {self.source!r})"


def parse_team(text):
    """'iyari, sigurd,moloch' → ['iyari', 'sigurd', 'moloch'] (пустые части пропускаются)."""
    return [t.strip() for t in text.split(",") if t.strip()]


def parse(window, decision):
    """Ответ на окно window. Возвращает (Answer, "") или (None, почему не понял)."""
    text = (decision or "").strip()
    head, colon, rest = text.partition(":")
    command, source = head.strip(), "gui"
    if command == "ROLLBACK_TG":
        command, source = "ROLLBACK", "telegram"
    if command not in ALLOWED[window]:
        return None, f"окно {WINDOW_NAMES[window]} такой команды не ждёт"
    if command in ("ROLLBACK", "NEW_PACK"):
        if command == "NEW_PACK" and not colon:
            return None, "в команде NEW_PACK нет пака"
        if colon:
            team = parse_team(rest)
            if not team:
                return None, "получен пустой пак"
            return Answer(command, team, source), ""
        return Answer(command, None, source), ""
    if colon:
        return None, f"у команды {command} не бывает продолжения после двоеточия"
    return Answer(command), ""
