from functions.get_files_info import get_files_info

if __name__ == "__main__":

    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)