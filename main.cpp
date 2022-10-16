#include <iostream>
#include "vector"

std::vector<double> years {1910., 1920., 1930., 1940., 1950., 1960., 1970., 1980., 1990., 2000.};
std::vector<double> people {92228496., 106021537., 123202624., 132164569., 151325798., 179323175.,
                         203211926., 226545805., 248709873., 281421906.};
std::vector<double> f2;
std::vector<double> f3;
std::vector<double> f4;
std::vector<double> f5;
std::vector<double> f6;
std::vector<double> f7;
std::vector<double> f8;
std::vector<double> f9;
std::vector<double> f10;
std::vector<std::vector<double>> f11;


int main() {
    f11.push_back(people);

    for(int i = 0; i < 9; ++i){
        f2.push_back((people[i] - people[i + 1]) / (years[i] - years[i + 1]));
    }
    f11.push_back(f2);

    for(int i = 0; i < 8; ++i){
        f3.push_back((f2[i] - f2[i + 1]) / (years[i] - years[i + 2]));
    }
    f11.push_back(f3);

    for(int i = 0; i < 7; ++i){
        f4.push_back((f3[i] - f3[i + 1]) / (years[i] - years[i + 3]));
    }
    f11.push_back(f4);

    for(int i = 0; i < 6; ++i){
        f5.push_back((f4[i] - f4[i + 1]) / (years[i] - years[i + 4]));
    }
    f11.push_back(f5);

    for(int i = 0; i < 5; ++i){
        f6.push_back((f5[i] - f5[i + 1]) / (years[i] - years[i + 5]));
    }
    f11.push_back(f6);

    for(int i = 0; i < 4; ++i){
        f7.push_back((f6[i] - f6[i + 1]) / (years[i] - years[i + 6]));
    }
    f11.push_back(f7);

    for(int i = 0; i < 3; ++i){
        f8.push_back((f7[i] - f7[i + 1]) / (years[i] - years[i + 7]));
    }
    f11.push_back(f8);

    for(int i = 0; i < 2; ++i){
        f9.push_back((f8[i] - f8[i + 1]) / (years[i] - years[i + 8]));
    }
    f11.push_back(f9);

    for(int i = 0; i < 1; ++i){
        f10.push_back((f9[i] - f9[i + 1]) / (years[i] - years[i + 9]));
    }
    f11.push_back(f10);


    double res = people[0];
    for(int i = 1; i < 10; ++i){
        double p = 1.;
        for(int j = 0; j < i; j++){
            p *= (2010. - years[j]);
        }
        p *= f11[i][0];
        res += p;
    }


    std::cout << "Extrapolated value : " << res << " " <<
     "and its error: " << std::abs(res - 308745538.);


    return 0;
}
