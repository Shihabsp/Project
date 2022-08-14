#include<iostream>
#include<string>

using namespace std;

void encode(string str, int letter)
{
    int number = letter-97;
    int capitalLast = 90-number;
    int lowerLast = 122-number;

    for(int i=0; i<str.length(); i++)
    {
        int sumNumber = 0;
        int temp = str[i];
        if(temp>=65 && temp<=capitalLast || temp>=97 && temp<=lowerLast){
            str[i] += number;
        }
        else if(temp>=capitalLast && temp<91){
            for(int i=capitalLast; i<91; i++){
                if(temp == i){
                    break;
                }
                sumNumber++;
            }
            str[i] = 64+sumNumber;
        }
        else if(temp>=lowerLast && temp<123){
            for(int i=lowerLast; i<123; i++){
                if(temp == i){
                    break;
                }
                sumNumber++;
            }
            str[i] = 96+sumNumber;
        }

    }
    cout<< "Encode: " << str << endl ;
}
int main()
{
    string text;
    cout << "Enter your name: ";
    getline(cin, text);

    char replacedLetter;
    cout << "Enter replaced letter what you want to: ";
    cin >> replacedLetter;

    cout << "Plaintext: " << text << endl ;

    encode(text, replacedLetter);
}