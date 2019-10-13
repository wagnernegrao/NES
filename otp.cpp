#include <iostream> 
#include <bitset> // Para conversao de string para binario
#include <string>
#include <string>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>

using namespace std;



int encrypt(int len){
    int i;

}

string createOpenText(string text){
    //string test1("wagner");
    string text_bin = "";
    for(int i = 0; i < text.size(); i++){
        bitset<8> bitset(text[i]);

        //cout << "c = " << c << endl;

        text_bin = text_bin + bitset.to_string<char,std::string::traits_type,std::string::allocator_type>();
    
    //cout << text_bin << endl;

    return(text_bin);
}