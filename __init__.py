# coding: utf-8
"""
Base for development of external modules.
To obtain the module / Function that is being called:
    GetParams ("module")

To obtain the variables sent from form / command Rocketbot:
    var = GetParams (variable)
    The "variable" is defined in forms of the package.json file

To modify the Rocketbot variable:
    SetVar (Variable_Rocketbot, "data")

To obtain a Rocketbot variable:
    var = GetVar (Variable_Rocketbot)

To obtain the selected option:
    option = GetParams ("option")


To install libraries you must enter the "libs" folder through the terminal

    pip install <package> -t.

"""

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "number2words" + os.sep + "libs" + os.sep
sys.path.append(cur_path)

from num2words import num2words


module = GetParams("module")

if module == "num2words":
    number = int(GetParams("number"))
    language = GetParams("language")
    result = GetParams("result")

    try:
        word = num2words(number, lang=language)
        SetVar(result, word)

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e