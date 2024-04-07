#include <iostream>

std::string FlagGen(int key) {
    if (key == 1337) { //kxctf{n1c3_try_:))} 19
        std::string fflag = "";
        fflag += "c3_";
        std::string fflag1 = "";
        for (int i = 2; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "1"; //_3c1
        fflag = "";
        for (int i = 3; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "t"; //1c3_t
        fflag1 = "";
        for (int i = 4; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "n"; //t_3c1n
        fflag = "";
        for (int i = 5; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "r"; //n1c3_tr
        fflag1 = "";
        for (int i = 6; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "{"; //rt_3c1n{
        fflag = "";
        for (int i = 7; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "y"; //{n1c3_try
        fflag1 = "";
        for (int i = 8; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "f"; //yrt_3c1n{f
        fflag = "";
        for (int i = 9; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "_"; //f{n1c3_try_
        fflag1 = "";
        for (int i = 10; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "t"; //_yrt_3c1n{ft
        fflag = "";
        for (int i = 11; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += ":"; //tf{n1c3_try_:
        fflag1 = "";
        for (int i = 12; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "c"; //:_yrt_3c1n{ftc
        fflag = "";
        for (int i = 13; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += ")"; //ctf{n1c3_try_:)
        fflag1 = "";
        for (int i = 14; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "x"; //):_yrt_3c1n{ftcx
        fflag = "";
        for (int i = 15; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += ")"; //xctf{n1c3_try_:))
        fflag1 = "";
        for (int i = 16; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "k"; //)):_yrt_3c1n{ftcxk
        fflag = "";
        for (int i = 17; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "}";
        fflag1 = "";
        return fflag;
    }
    else if (key != 1337) { //NN4GG5DGPN2V6YLDG52TI3DMPFPWOMBQMR6Q====
        std::string fflag = "";
        fflag += "YLDG52TI3";
        std::string fflag1 = "";
        for (int i = 8; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "6V2";
        fflag = "";
        for (int i = 11; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "DM";
        fflag1 = "";
        for (int i = 13; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "NPGD";
        fflag = "";
        for (int i = 17; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "PFP";
        fflag1 = "";
        for (int i = 20; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "5GG";
        fflag = "";
        for (int i = 23; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "WOMB";
        fflag1 = "";
        for (int i = 27; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "4NN";
        fflag = "";
        for (int i = 30; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "QMR6Q";
        fflag1 = "";
        for (int i = 35; i >= 0; i--) {
            fflag1 += fflag[i];
        }
        fflag1 += "";
        fflag = "";
        for (int i = 35; i >= 0; i--) {
            fflag += fflag1[i];
        }
        fflag += "====";
        fflag1 = "";
        return fflag;
    }
    return "kxctf{...";
}


int main()
{
    int n;
    std::cin >> n;
    FlagGen(n);
    std::cin.get();
    return 0;
}
