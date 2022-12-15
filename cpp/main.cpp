#include <iostream>


//Function 
void findNumType(int number1, float number2)
{
  std::cout<<"The integer is: "<<number1<<"\n";
  std::cout<<"The double is: "<<number2<<"\n";
}

int main()
{
  std::cout<<"    \n";

//Function 
  int type1 = 280;
  float type2 = 20.356;

findNumType(type1, type2);

  std::cout<<"    \n";

//Print Hello World!
  std::cout<<"Hello World!\n"; 

  std::cout<<"      \n";

//If statement
int num = 16;
if(num % 2 == 0)
{
  std::cout<<"The number is even.\n";
}
else
{
  std::cout<<"The number is odd.\n"; 
}

  std::cout<<"         \n";

//A loop
int age = 1;
while(age<18)
{
  std::cout<<"At the age of "<<age<<" you cannot vote."<<std::endl;
  age = age + 1;
}

  return 0;
}