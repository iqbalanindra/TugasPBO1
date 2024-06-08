class Employee:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__salary = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary


# Program Utama dengan tema TKJ
if __name__ == "__main__":
    # Membuat objek karyawan
    employee = Employee()

    # Mengatur detail karyawan
    employee.set_name("Iqbal lulusan sekolah TKJ Student")
    employee.set_age(19)
    employee.set_salary(0)  # Siswa biasanya tidak memiliki gaji

    # Mendapatkan dan menampilkan detail karyawan
    print("Employee Details:")
    print("Nama dan Jurusan:", employee.get_name())
    print("Age:", employee.get_age())
    print("Salary:", employee.get_salary())  # Siswa tidak memiliki gaji, tetapi kita tampilkan untuk konsistensi
