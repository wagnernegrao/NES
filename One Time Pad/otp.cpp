#include <iostream>
#include <string>
#include <bitset> // Para conversao de string para binario
#include <random>
#include <ctime>

using namespace std;

string createOpenText (string text);
int generateRandom();
string generateKey (int key_size);
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

        bitset<8> bitset(text[i]); // Convert 1 caracter em 8 bits

        // Converte os bits em string e adiciona na lista
        text_bin = text_bin + bitset.to_string<char,std::string::traits_type,std::string::allocator_type>();
    }

    return(text_bin);
}

int generateRandom(){
    random_device random_device;
    mt19937 random_engine(random_device());
    uniform_int_distribution<long int> distribution_1_100(1, 9999999999999);

    auto const randomNumber = distribution_1_100(random_engine);

    return(randomNumber);
}

string generateKey (int key_size){
    string key = "";

    for(int i = 0; i < key_size; i++){
        if(generateRandom()%2 == 1){
            key += "1";
        }else{
            key += "0";
        }
    } 

    return(key);
}

string encrypt (string open_text, string key){
    string encrypt_text = "";

    // Faz a operacao xor para criptografar
    for(int i = 0; i < open_text.size(); i++){
    
        encrypt_text = encrypt_text + to_string(open_text[i] ^ key[i]);
    }

    return(encrypt_text);
}

string decrypt (string encrypt_text, string key){
    string decrypt_text = "";

    // Faz a operacao xor para decriptografar
    for(int i = 0; i < encrypt_text.size(); i++){
    
        decrypt_text = decrypt_text + to_string(encrypt_text[i] ^ key[i]);
    }

    return(decrypt_text);
}