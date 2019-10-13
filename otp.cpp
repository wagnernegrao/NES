#include <iostream> 
#include <bitset> // Para conversao de string para binario
#include <string>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

string createOpenText (string text);
string generateKey (int size);
string encrypt (string open_text, string key);
string decrypt (string encrypt_text, string key);


int main(){
  string open_text;
  string text_bin;
  string key;
  string encrypt_text;
  string decrypt_text;


  cout << "Adicione o texto: ";
  getline (cin, open_text);
  

  text_bin = createOpenText(open_text);

  cout << "Text bin: " << text_bin << endl;

  key = generateKey(text_bin.size());

  cout << "Text key: " << key << endl;

  encrypt_text = encrypt(text_bin, key);

  cout << "Text cri: " << encrypt_text << endl;

  decrypt_text = decrypt(encrypt_text, key);

  cout << "Text dec: " << decrypt_text << endl;


}

string createOpenText (string text){
    string text_bin = "";

    for(int i = 0; i < text.size(); i++){

        bitset<8> bitset(text[i]);
        text_bin = text_bin + bitset.to_string<char,std::string::traits_type,std::string::allocator_type>();
    }

    return(text_bin);
}

string generateKey (int size){
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

string encrypt (string open_text, string key){
    string encrypt_text = "";

    for(int i = 0; i < open_text.size(); i++){
    
        encrypt_text = encrypt_text + to_string(open_text[i] ^ key[i]);
    }

    return(encrypt_text);
}

string decrypt (string encrypt_text, string key){
  string decrypt_text = "";

  for(int i = 0; i < encrypt_text.size(); i++){
    
    decrypt_text = decrypt_text + to_string(encrypt_text[i] ^ key[i]);
  }

  return(decrypt_text);
}