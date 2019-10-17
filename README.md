# NES (Network Encryption and Security)

This is a repository to add algorithms to cryptology.

Was implemented:

- [x] OTP (One Time Pad)
- [x] AES (Advanced Encryption Standard)
- [x] 3DES (Triple Data Encryption Standard)
- [ ] ?


You can add other algorithms to cryptology, feel free to contribute.


## Dependencies

### Python
```sh
pip install pycrypto
pip install cryptography
```

### C++
```sh
sudo apt-get install gcc
```

## How to run
### Run python
You must use the Python 3.5 version or version more actualized.
```
$ python3 3DES.py

$ python3 AES.py
```
### Run C++
Compile:

```g++
g++ -std=c++11 otp.cpp
```

Run:
```g++
./a.out
```
## Licence
[MIT](https://github.com/wagnernegrao/NES/blob/master/LICENSE)