#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct flag {
    char* flag;
};

struct student {
    char* name;
};

struct teacher {
    char* name;
    unsigned int studentsNumber;
    struct student** students;  
};

#define MAX_STUDENTS 10
#define MAX_TEACHERS 10

struct flag* f;
unsigned int studentsNumber = 0;
unsigned int teachersNumber = 0;

struct student* students[MAX_STUDENTS];
struct teacher* teachers[MAX_TEACHERS];

struct flag* createFlag() {
    struct flag* f = malloc(sizeof(struct flag));
    f->flag = getenv("FLAG");
    return f;
}

struct student* createStudent(char* name) {
    struct student* s = malloc(sizeof(struct student));    
    s->name = name;
    return s;
}

struct teacher* createTeacher(char* name) {
    struct teacher* t = malloc(sizeof(struct teacher));
    t->name = name;
    t->students = malloc(sizeof(struct student*)*MAX_STUDENTS);
    t->studentsNumber = 0;
    return t; 
}

void banner() {
    printf(" ________________________________________________________________________ \n");
    printf("|    __  ___________  _________       _____ __    ___ _    _____________ |\n");
    printf("|   /  |/  /  _/ __ \\/ ____/   |     / ___// /   /   | |  / / ____/ ___/ |\n");
    printf("|  / /|_/ // // /_/ / __/ / /| |     \\__ \\/ /   / /| | | / / __/  \\__ \\  |\n");
    printf("| / /  / // // _, _/ /___/ ___ |    ___/ / /___/ ___ | |/ / /___ ___/ /  |\n");
    printf("|/_/  /_/___/_/ |_/_____/_/  |_|   /____/_____/_/  |_|___/_____//____/   |\n");
    printf("|________________________________________________________________________|\n\n");

}

void printHelloMessage() {
    printf("Hello, Director of MIREA!\nHere you can see your students and whose slaves they are!\n\n");
}

void printHelpMessage() {
    printf("What can you do:\n\n1. Print student\n2. Print teacher\n3. Print all students\n4. Print all teachers\n5. Add student\n6. Add teacher\n7. Link a student to a teacher by making him a slave\n8. Delete student\n9. Delete teacher\n10. Allocate flag\n11. Exit\n\nEnter your choice: ");
}

unsigned int getStudentIndex() {
    printf("Students: \n");
    for (int i = 0; i < studentsNumber; ++i) {
        printf("\t%d. %s\n", i+1, students[i]->name);
    }

    unsigned int studentIndex;

    printf("Enter the student index to link: ");
    fflush(stdout);
    scanf("%2d", &studentIndex);

    studentIndex -= 1;
    return studentIndex;
}

unsigned int getTeacherIndex() {
    printf("\nTeachers: \n");
    for (int i = 0; i < teachersNumber; ++i) {
        printf("\t%d. %s\n", i+1, teachers[i]->name);
    }

    unsigned int teacherIndex;

    printf("Enter the teacher index to link: ");
    fflush(stdout);
    scanf("%2d", &teacherIndex);

    teacherIndex -= 1;
    return teacherIndex;
} 

void printStudent() {
    if (studentsNumber == 0) {
        printf("There are no students yet!\n");
        return;
    }

    unsigned int studentIndex = getStudentIndex();

    if (studentIndex >= studentsNumber) {
        printf("Index is too big:(\n\n");
        return;
    }

    printf("<Student info> \n\t- Name: %s\n\n", students[studentIndex]->name);
}

void printTeacher() {
    if (teachersNumber == 0) {
        printf("There are no teachers yet!\n");
        return;
    }
    unsigned int teacherIndex = getTeacherIndex();

    if (teacherIndex >= teachersNumber) {
        printf("Index is too big:(\n\n");
        return;
    }

    printf("<Teacher info>\n\t- Name: %s\n", teachers[teacherIndex]->name);

    if (teachers[teacherIndex]->studentsNumber == 0) { 
        printf("\t- No slaves:(\n\n");
        return;
    }
    
    printf("\t- Slaves:\n");

    for (int i = 0; i < teachers[teacherIndex]->studentsNumber; ++i) {
        printf("\t\t- %s\n", teachers[teacherIndex]->students[i]->name);
    }
    printf("\n");
}

void printStudents() {
    if (studentsNumber == 0) {
        printf("There are no students yet!\n");
        return;
    }

    printf("Here is a students (slaves) list (quantity: %d):\n", studentsNumber);
    for (int i = 0; i < studentsNumber; ++i) {
        printf("\t%d. %s\n", i+1, students[i]->name);
    }
    printf("\n");
}

void printTeachers() {
    if (teachersNumber == 0) {
        printf("There are no teachers yet!\n");
        return;
    }

    printf("Here is a teachers list (quantity: %d):\n", teachersNumber);
    for (int i = 0; i < teachersNumber; ++i) {
        printf("\t%d. %s\n", i+1, teachers[i]->name);
    }
    printf("\n");
}

void addStudent() {
    if (studentsNumber >= MAX_STUDENTS) {
        printf("Students number is too big! Try to expel someone (hohoho)!!!\n\n");
        return;
    }

    char* name = malloc(sizeof(char) * 11);
    printf("Enter the name of the new student: ");
    fflush(stdout);
    scanf("%10s", name);
    students[studentsNumber] = createStudent(name);
    studentsNumber += 1;

    printf("The student has been successfully added!\n\n");
}

void addTeacher() {
    if (teachersNumber >= MAX_TEACHERS) {
        printf("Teachers number is too big! Try to dismiss someone (hohoho)!!!\n\n");
        return;
    }

    char* name = malloc(sizeof(char) * 11);
    printf("Enter the name of the new teacher: ");
    fflush(stdout);
    scanf("%10s", name);
    teachers[teachersNumber] = createTeacher(name);
    teachersNumber += 1;

    printf("The teacher has been successfully added!\n\n");
}

void linkStudentToTeacher() {
    if (studentsNumber == 0 || teachersNumber == 0) {
        printf("Our university staff has not been completed yet!");
        return;
    }

    unsigned int studentIndex = getStudentIndex();
    
    if (studentIndex >= studentsNumber) {
        printf("Invalid student index!\n\n");
        return;
    }

    unsigned int teacherIndex = getTeacherIndex();

    if (teacherIndex >= teachersNumber) {
        printf("Invalid teacher index!\n\n");
        return;
    }

    unsigned int linkedStudentsNumber = teachers[teacherIndex]->studentsNumber; 

    if (linkedStudentsNumber >= MAX_STUDENTS) {
        printf("Too much linked students!\n\n");
        return;
    }

    for (int i = 0; i < linkedStudentsNumber; ++i) {
        if (teachers[teacherIndex]->students[i] == students[studentIndex]) {
            printf("This student is already linked to this teacher!!\n\n");
            return;
        }
    }

    printf("%d", linkedStudentsNumber);
    teachers[teacherIndex]->students[linkedStudentsNumber] = students[teacherIndex];
    teachers[teacherIndex]->studentsNumber += 1;
    printf("Successfully linked!! The student %s became a slave to the teacher %s!\n\n", students[studentIndex]->name, teachers[teacherIndex]->name);
}

void deleteStudent() {
    if (studentsNumber == 0) {
        printf("There are no students yet!\n");
        return;
    }

    unsigned int studentIndex = getStudentIndex();

    if (studentIndex >= studentsNumber) {
        printf("Index is too big:(\n\n");
        return;
    }

    free(students[studentIndex]->name);
    free(students[studentIndex]);

    for (int i = studentIndex; i < studentsNumber - 1; ++i){
        students[i] = students[i+1];
    } 
    studentsNumber -= 1;
    
    printf("The student was successfully deleted\n\n");
}

void deleteTeacher() {
    if (teachersNumber == 0) {
        printf("There are no teachers yet!\n");
        return;
    }

    unsigned int teacherIndex = getTeacherIndex();

    if (teacherIndex >= teachersNumber) {
        printf("Index is too big:(\n\n");
        return;
    }

    free(teachers[teacherIndex]->students);
    free(teachers[teacherIndex]->name);
    free(teachers[teacherIndex]);
    
    for (int i = teacherIndex; i < teachersNumber - 1; ++i){
        teachers[i] = teachers[i+1];
    }

    teachersNumber -= 1;

    printf("The student was successfully deleted!!\n\n");
}

void quit() {
    for (int i = 0; i < studentsNumber; ++i) {
        free(students[i]->name);
        free(students[i]);
    }
    
    for (int i = 0; i < teachersNumber; ++i) {
        free(teachers[i]->name);
        free(teachers[i]->students);
        free(teachers[i]);
    }
    
    if (f) {
        free(f);
    }
}


void main() {
    banner();

    printHelloMessage();
    unsigned int mode;

    while (true) {
        printHelpMessage();
        fflush(stdout);
        mode = 0;
        scanf("%2d", &mode);
        printf("\n");
        switch (mode){
            case 1: {
                printStudent();
                break;
            }
            case 2: {
                printTeacher();
                break;
            }
            case 3: {
                printStudents();
                break;
            }
            case 4: {
                printTeachers();
                break;
            }
            case 5: {
                addStudent();
                break;
            }
            case 6: {
                addTeacher();
                break;
            }
            case 7: {
                linkStudentToTeacher();
                break;
            }
            case 8: {
                deleteStudent();
                break;
            }
            case 9: {
                break;
            }
            case 10: {
                f = createFlag();
                break;
            }
            default: {
                quit();
                return;
            }
        }
    }
}