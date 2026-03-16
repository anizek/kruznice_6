



















































# def analyze_password(password, min_length, require_digit, require_upper, require_symbol, banned_words):
#     pocet_pravidel = 4
#     porusena_pravidla = 0
#     lis = []
#     if len(password) <= min_length:
#         porusena_pravidla += 1
#         lis.append("min_length")
#     for i in password:
#         if i.isdigit() != require_digit:
#             porusena_pravidla += 1
#             lis.append("require_digit")
#             break
#     for i in password:
#         if i.isupper() != require_upper:
#             porusena_pravidla += 1
#             lis.append("require_upper")
#             break
#     for i in password:
#         if i in ["!@#$%^&*()-_=+[]{};:,.?"]:
#             porusena_pravidla =+ 1
#             lis.append("require_symbol")
#             break
#     if porusena_pravidla > 0:
#         is_strong = False
#     procenta = (porusena_pravidla/pocet_pravidel) * 100
#     return is_strong, procenta, lis
#
#
#
#
#
#
# print(analyze_password("tvojemama67!",
#                  8,
#                  True,
#                  True,
#                  True,
#                  ["heslo", "1234"]))


