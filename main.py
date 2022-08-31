from pytest import main


def join_01(xs, delimiter: str) -> str:
    re = delimiter.join(str(x) for x in xs)
    return re


# if __name__ == "__main__":
#
#     print(join_01([1, 2, 3], "==="))

main(['-vv'])  # c'est pour executer directement les tests
