from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

if __name__ == "__main__":

    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)

    # result = get_file_content("calculator", "lorem.txt")
    # print("Result for lorem.txt:")
    # print(result)

    # result = get_file_content("calculator", "main.py")
    # print("Result for main.py:")
    # print(result)

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for pkg/calculator.py:")
    # print(result)

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for /bin/cat:")
    # print(result)

    # result = get_file_content("calculator", "pkg/does_not_exist.py")
    # print("Result for pkg/does_not_exist.py:")
    # print(result)

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for write to lorem.txt:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for write to pkg/morelorem.txt:")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for write to /tmp/temp.txt:")
    print(result)