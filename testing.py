
def test(class_name, methods, name):
    return f"class {class_name} {methods} {name}"


class_name = "test"
methods = "public static void "
name = "main(String[ ] arg) {}"
test = """ class Test {
    pulic static void main(String[ ] arg) {
        // this is a test 
    }
}
"""


with open('testing.txt', mode='w') as w:
    w.writelines(test)

