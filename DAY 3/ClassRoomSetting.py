from streamlit import empty


def classroom_setting(arr):
    rows=3
    columns=3
    for i in range(rows):
        for j in range(columns):
            print(arr[i][j],end=" ")
        print()