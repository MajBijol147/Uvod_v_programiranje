# =============================================================================
# Kolokviji
#
# V vsaki vrstici datoteke imamo shranjene rezultate kolokvija v obliki:
#
#     Ime Priimek,N1,N2,N3,N4,N5
#
# Cela števila od `N1` do `N5` predstavljajo število točk pri posamezni nalogi.
# Zgled:
#
#     Janez Novak,1,3,3,0,2
# =====================================================================@001518=
# 1. podnaloga
# Sestavite funkcijo `nabor`, ki kot parameter dobi niz z vejico ločenih
# vrednosti v taki obliki, kot je opisano zgoraj. Funkcija naj vrne nabor s
# temi vrednostmi. Pri tem naj točke za posamezne naloge spremeni v števila
# (tj. naj jih ne vrača kot nize).
#
#     >>> nabor('Janez Novak,1,3,3,0,2')
#     ('Janez Novak', 1, 3, 3, 0, 2)
#     >>> nabor('Janez Horvat,2,4,0')
#     ('Janez Horvat', 2, 4, 0)
#
# Predpostavite lahko, da so vsi podatki razen prvega res števila. Ni pa nujno,
# da imenu sledi natanko 5 števil.
# =============================================================================
def nabor(niz):
    sez = niz.rsplit(",")
    podatki = []
    for k in sez:
        if k == "":
            pass
        elif k.isdigit() == True:
            podatki.append(int(k))
        else:
            podatki.append(k)
    return tuple(podatki)


# =====================================================================@001519=
# 2. podnaloga
# Sestavite funkcijo `nalozi_csv`, ki kot parameter dobi ime datoteke, v kateri
# se nahajajo rezultati kolokvija. Vrstice v tej datoteki so take oblike, kot
# je opisano zgoraj. Funkcija naj vrne seznam naborov; za vsako vrstico po
# enega.
#
# Primer: Če so v datoteki kolokviji.txt shranjeni naslednji podatki:
#
#     Janez Novak,1,3,3,0,2
#     Peter Klepec,1,0,1,2,1,3
#     Drago Dragić,7
#
# potem
#
#     >>> nalozi_csv('kolokviji.txt')
#     [('Janez Novak', 1, 3, 3, 0, 2), ('Peter Klepec', 1, 0, 1, 2, 1, 3), ('Drago Dragić', 7)]
# =============================================================================
def nalozi_csv(vhod):
    nabori = []
    with open(vhod, encoding="utf-8") as vh:
        for vrstica in vh:
            nabori.append(nabor(vrstica.rstrip()))
    return nabori


# =====================================================================@001520=
# 3. podnaloga
# Sestavite funkcijo `vsote`, ki sprejme imeni vhodne in izhodne datoteke. Iz
# prve naj prebere vrstice s podatki (ki so v taki obliki, kot je opisano
# zgoraj), nato pa naj izračuna vsoto točk za vsakega študenta in v drugo
# datoteko shrani podatke v obliki:
#
#     Ime Priimek,vsota
#
# Za vsako vrstico v vhodni datoteki morate zapisati ustrezno vrstico v izhodno
# datoteko.
#
# Primer: Če je v datoteki kolokviji.txt enaka vsebina kot pri prejšnji
# podnalogi, potem naj bo po klicu `vsote('kolokviji.txt', 'sestevki.txt')` v
# datoteki sestevki.txt naslednja vsebina:
#
#     Janez Novak,9
#     Peter Klepec,8
#     Drago Dragić,7
# =============================================================================
def vsote(vhod, izhod):
    vsote = []
    podatki = nalozi_csv(vhod)
    for podatek in podatki:
        vsota = sum(podatek[1:])
        vsote.append(podatek[0] + "," + str(vsota))
    with open(izhod, "w", encoding="utf-8") as iz:
        for oseba in vsote:
            print(oseba, file=iz)


# =====================================================================@001521=
# 4. podnaloga
# Sestavite funkcijo `rezultati`, ki sprejme imeni vhodne in izhodne datoteke.
# Iz prve naj prebere vrstice s podatki, v drugo pa naj zapiše originalne
# podatke, skupaj z vsotami (na koncu dodajte še en stolpec). Predpostavite, da
# je v vsaki vrstici enako število ocen po posameznih nalogah.
#
# V zadnjo vrstico naj funkcija zapiše še povprečne ocene po posameznih
# stolpcih, zaokrožene in izpisane na dve decimalni mesti. Ime v tej vrstici
# naj bo `POVPRECEN STUDENT`.
#
# V izhodni datoteki naj bodo vrstice urejene po priimkih (razen zadnje
# vrstice, v kateri so povprečja). Predpostavite, da ima vsak študent eno ime
# in en priimek, ki sta ločena s presledkom. Ne pozabite na povprečje vsot!
#
# Primer: Če je na datoteki kolokviji.txt vsebina
#
#     Janez Novak,1,3,3,2,0
#     Micka Kovač,0,3,2,2,3
#     Peter Klepec,1,0,1,2,1
#
# naj bo po klicu funkcije `rezultati('kolokviji.txt', 'rezultati.txt')` na
# datoteki rezultati.txt naslednja vsebina:
#
#     Peter Klepec,1,0,1,2,1,5
#     Micka Kovač,0,3,2,2,3,10
#     Janez Novak,1,3,3,2,0,9
#     POVPRECEN STUDENT,0.67,2.00,2.00,2.00,1.33,8.00
# =============================================================================
def rezultati(vhodna, izhodna):
    seznam = nalozi_csv(vhodna)
    # Izračunamo vsote po vrsticah
    n = len(seznam)
    for i in range(n):
        seznam[i] = seznam[i] + (sum(seznam[i][1:]),)
    # Sortiramo po priimkih
    seznam.sort(key=lambda x: x[0].split(' ')[1])
    # Izračunamo povprečja po stolpcih
    m = len(seznam[0])
    povpr = ['POVPRECEN STUDENT'] + ['{0:.2f}'.format(sum(seznam[i][j] for i in range(n)) / n) for j in range(1, m)]
    seznam.append(tuple(povpr))
    # Zapišemo podatke na izhodno datoteko
    with open(izhodna, 'w', encoding='utf-8') as f:
        for vrstica in seznam:
            print(','.join(str(x) for x in vrstica), file=f)

# ============================================================================@
# fmt: off
"Če vam Python sporoča, da je v tej vrstici sintaktična napaka,"
"se napaka v resnici skriva v zadnjih vrsticah vaše kode."

"Kode od tu naprej NE SPREMINJAJTE!"

# isort: off
import json
import os
import re
import shutil
import sys
import traceback
import urllib.error
import urllib.request
import io
from contextlib import contextmanager


class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end="")
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end="")
        return line


class TimeoutError(Exception):
    pass


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part["solution"].strip() != ""

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part["valid"] = True
            part["feedback"] = []
            part["secret"] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part["feedback"].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part["valid"] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part["secret"].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                "Izraz {0} vrne {1!r} namesto {2!r}.",
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for x, v in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part["feedback"][:]
        yield
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part["feedback"][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print("{0}. podnaloga je brez rešitve.".format(i + 1))
            elif not part["valid"]:
                print("{0}. podnaloga nima veljavne rešitve.".format(i + 1))
            else:
                print("{0}. podnaloga ima veljavno rešitev.".format(i + 1))
            for message in part["feedback"]:
                print("  - {0}".format("\n    ".join(message.splitlines())))

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield

    @staticmethod
    @contextmanager
    def time_limit(timeout_seconds=1):
        from signal import SIGINT, raise_signal
        from threading import Timer

        def interrupt_main():
            raise_signal(SIGINT)

        timer = Timer(timeout_seconds, interrupt_main)
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            raise TimeoutError
        finally:
            timer.cancel()


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding="utf-8") as f:
            source = f.read()
        part_regex = re.compile(
            r"# =+@(?P<part>\d+)=\s*\n"  # beginning of header
            r"(\s*#( [^\n]*)?\n)+?"  # description
            r"\s*# =+\s*?\n"  # end of header
            r"(?P<solution>.*?)"  # solution
            r"(?=\n\s*# =+@)",  # beginning of next part
            flags=re.DOTALL | re.MULTILINE,
        )
        parts = [
            {"part": int(match.group("part")), "solution": match.group("solution")}
            for match in part_regex.finditer(source)
        ]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]["solution"] = parts[-1]["solution"].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = "{0}.{1}".format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    "part": part["part"],
                    "solution": part["solution"],
                    "valid": part["valid"],
                    "secret": [x for (x, _) in part["secret"]],
                    "feedback": json.dumps(part["feedback"]),
                }
                if "token" in part:
                    submitted_part["token"] = part["token"]
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode("utf-8")
        headers = {"Authorization": token, "content-type": "application/json"}
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response["attempts"]:
            part["feedback"] = json.loads(part["feedback"])
            updates[part["part"]] = part
        for part in old_parts:
            valid_before = part["valid"]
            part.update(updates.get(part["part"], {}))
            valid_after = part["valid"]
            if valid_before and not valid_after:
                wrong_index = response["wrong_indices"].get(str(part["part"]))
                if wrong_index is not None:
                    hint = part["secret"][wrong_index][1]
                    if hint:
                        part["feedback"].append("Namig: {}".format(hint))

    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjoxNTE4LCJ1c2VyIjoxMDczMH0:1uNwhw:Yby0RinrIqip7Nn8jLGpwXDgti03ZbG_-DRb7amOIT0"
        try:
            Check.equal('nabor("Janez Novak,1,3,3,0,2")', ("Janez Novak", 1, 3, 3, 0, 2))
            Check.equal('nabor("Janez Horvat,2,4,0")', ("Janez Horvat", 2, 4, 0))
            Check.equal('nabor("Micka Kovačeva,0,3,2,2,3")', ("Micka Kovačeva", 0, 3, 2, 2, 3))
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjoxNTE5LCJ1c2VyIjoxMDczMH0:1uNwhw:eMPAL0KnZOPHWeHrxV7kdFoFVLj-VIzj1rVdgfT24M8"
        try:
            test_data = [
                ("kolokviji_vhod.txt", ["Janez Novak,1,3,3,2,0", "Micka Kovaceva,0,3,2,3", "Miha Praznic", "Peter Klepec,1,0,1,2,1,3"],
                 'nalozi_csv("kolokviji_vhod.txt")', [("Janez Novak", 1, 3, 3, 2, 0), ("Micka Kovaceva", 0, 3, 2, 3), ("Miha Praznic",), ("Peter Klepec", 1, 0, 1, 2, 1, 3)]),
            ]
            napaka = False
            for vhodna, vhod, klic, izhod in test_data:
                if napaka: break
                with Check.in_file(vhodna, vhod, encoding='utf-8'):
                    if not Check.equal(klic, izhod):
                        napaka = True # test has failed
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjoxNTIwLCJ1c2VyIjoxMDczMH0:1uNwhw:YbILOUm9jzh0FWpBSc-a2guTk11r7uGGdyn1rkxIB7g"
        try:
            test_data = [
                ("kolokviji_vhod.txt", ["Janez Novak,1,3,3,2,0", "Micka Kovaceva,0,3,2,3", "Miha Praznic", "Peter Klepec,1,0,1,2,1,3"],
                 "kolokviji_izhod.txt",  ["Janez Novak,9", "Micka Kovaceva,8", "Miha Praznic,0", "Peter Klepec,8"]),
            ]
            napaka = False
            for vhodna, vhod, izhodna, izhod in test_data:
                if napaka: break
                with Check.in_file(vhodna, vhod, encoding='utf-8'):
                    vsote(vhodna, izhodna)
                    if not Check.out_file(izhodna, izhod, encoding='utf-8'):
                        napaka = True
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjoxNTIxLCJ1c2VyIjoxMDczMH0:1uNwhw:GHUbN1K6FiZgtw7tJXSmpCNDI48sI--vRGvVImg78MU"
        try:
            test_data = [
                ("kolokviji_vhod2.txt", ["Janez Novak,1,3,3,2,0", "Micka Kovac,0,3,2,2,3", "Peter Klepec,1,0,1,2,1"],
                 "kolokviji_izhod2.txt", ["Peter Klepec,1,0,1,2,1,5", "Micka Kovac,0,3,2,2,3,10", "Janez Novak,1,3,3,2,0,9", "POVPRECEN STUDENT,0.67,2.00,2.00,2.00,1.33,8.00"]),
            ]
            napaka = False
            for vhodna, vhod, izhodna, izhod in test_data:
                if napaka: break
                with Check.in_file(vhodna, vhod, encoding='utf-8'):
                    rezultati(vhodna, izhodna)
                    if not Check.out_file(izhodna, izhod, encoding='utf-8'):
                        napaka = True # test has failed
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        url = "https://www.projekt-tomo.si/api/attempts/submit/"
        token = "Token a7b4c86b50d1961be0f245c0e6645ecd9d6f34ab"
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = (
            "\n"
            "-------------------------------------------------------------------\n"
            "PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n"
            "Preberite napako in poskusite znova ali se posvetujte z asistentom.\n"
            "-------------------------------------------------------------------\n"
        )
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print("Rešitve so shranjene.")
        update_attempts(Check.parts, response)
        if "update" in response:
            print("Updating file... ", end="")
            backup_filename = backup(filename)
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(response["update"])
            print("Previous file has been renamed to {0}.".format(backup_filename))
            print("If the file did not refresh in your editor, close and reopen it.")
    Check.summarize()


if __name__ == "__main__":
    _validate_current_file()
