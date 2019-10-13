#include <iostream> 
#include <bitset> // Para conversao de string para binario
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

string createCloseText(int size){
    string key = "";

    for(int i = 0; i < size; i++){
        if(rand()%2 == 1){
            key += "1";
        }else{
            key += "0";
        }
    } 

    return(key);
}

string encrypt(string text, string key){
    string encrypt_text = "";

    for(int i = 0; i < v1.size(); i++){
    
        encrypt_text = encrypt_text + to_string(text[i] ^ key[i]);

        //cout << ( text[i] ^ key[i] ) << endl;
    }
    //cout << "v3 :" << v3 << endl;
    return(encrypt_text);
}