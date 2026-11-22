#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdlib>
using namespace std;
void showVar(){ static int var = 10; cout << var << " "; var++; }
void showVar2(){ int var = 10; cout << var << " "; var++; }
void addVal(int n){ n = n + 37; }
void addRef(int &n){ n = n + 37; }
int getSum(int a, int b = 0, int c = 0){ return a + b + c; }
int sum(int, int);
bool isEven(int n){ return n % 2 == 0; }
int gx; int gy = 5;
void shadow(){ int gy = 99; cout << gy; }
void dims(int a){ cout << "int "; } void dims(int a,int b){ cout << "int,int "; }
void dims(int a,double b){ cout << "int,double "; } void dims(double a,double b){ cout << "double,double "; }
int main(){
 cout << "AND/OR: "; { int x=12,y=5,z=-4; cout << ((x>y)&&(y>z)) << ((x<=z)||(y==z)) << !(x>=z); } cout << "\n";
 cout << "sum1-10: "; { int s=0,c=1; while(c<=10){ s+=c; c++; } cout << s; } cout << "\n";
 cout << "trace: " << 10*15 << " " << 2*(10+15) << " " << 20*20 << " " << 2*(20+20) << "\n";
 cout << "7?3: " << 7+3 << " " << 7-3 << " " << 7*3 << " " << 7/3 << " " << 7%3 << " " << 13/5.0 << " " << 7/3.0 << "\n";
 cout << "prec: " << 2 + 2 * 2 - 2 << " " << (2 + 2) * 2 - 2 << " " << pow(4,2) << "\n";
 { int r = 3.88; int x = 3.9; cout << "trunc: " << r << " " << x << "\n"; }
 { int kira=5; int v = 5*kira-- + 10; cout << "kira: " << v << " " << kira << "\n"; }
 { int i=10,j=2; i*=j+3; int a=4; a+=3; int x,y,z; x=y=z=5; cout << "comb: " << i << " " << a << " " << x+y+z << "\n"; }
 { char ch='C'; cout << "cast: " << (int)ch << " " << int(ch) << " " << static_cast<double>(7)/2 << " " << 'A'+1 << " " << sizeof(char) << sizeof(int) << sizeof(double) << sizeof(bool) << "\n"; }
 cout << "bool: " << 2 + true << " " << (bool)-10 << " " << (bool)0 << "\n";
 { int x = 20; cout << "2<x<9 x=20: " << (2 < x < 9) << " proper: " << (2<x && x<9) << "\n"; }
 { int n = 5; cout << "!n>9: " << (!n > 9) << " !(n>9): " << !(n>9) << "\n"; }
 { int x = 5; if ((x = 0)) cout << "T"; else cout << "F"; cout << " x=" << x << "\n"; }
 { int x = 1; if (x<3); cout << "semi-ran"; x = 7; if (x<3); cout << " again\n"; }
 { int a=5,b=1; if (a>3) if (b>3) cout << "X"; else cout << "Y"; cout << "\n"; }
 { int p=3,q=8; p = (p<5) ? q+1 : 5; cout << "tern: " << p << " "; p=7; p = (p<5) ? q+1 : 5; cout << p << "\n"; }
 { int n=-7; cout << "n%2: " << (n%2 ? "odd" : "even") << "\n"; }
 { char grade='B'; switch(grade){ case 'A': cout << "Excellent!"; break; case 'B': cout << "Very good!"; break; case 'C': cout << "Good"; break; default: cout << "Fail"; } cout << "\n"; }
 { char grade='C'; switch(grade){ case 'A': cout << "Excellent!"; case 'B': cout << "Very good!"; case 'C': cout << "Good"; default: cout << "Fail"; } cout << "\n"; }
 { int n=10; while(n>0){ cout << n << " "; n=n-1; } cout << "| "; for(n=10;n>0;n--) cout << n << " "; cout << "| "; n=10; do{ cout << n << " "; n=n-1; } while(n>0); cout << "\n"; }
 { int n=0; do { cout << "once "; } while (n > 0); n=0; while (n > 0) cout << "never"; cout << "\n"; }
 { int n; for(n=10;n>0;n--){ if(n<8) break; cout<<n; } cout << " | "; for(n=10;n>0;n--){ if(n<8) break; cout<<n<<" "; } cout << "\n"; }
 { int n; for(n=10;n>0;n--){ if(n%2==1) continue; cout<<n<<" "; } cout << "\n"; }
 { int n=9, g=0; while(n>0 && g<5){ g++; cout << n << " "; if (n%2==1) continue; n = n - 1; } cout << "(guarded)\n"; }
 { int c=0; for(int i=0;i<3;i++) for(int j=0;j<3;j++) c++; cout << "3x3: " << c << " "; c=0; for(int i=0;i<4;i++) for(int j=0;j<2;j++) c++; cout << c << "\n"; }
 { int c=0; for(int i=0;i<3;i++){ for(int j=0;j<5;j++){ if(j==2) break; c++; } } cout << "nested break: " << c << "\n"; }
 cout << "strcmp: " << strcmp("abc","abc") << " strlen: " << strlen("George") << " strstr: " << (strstr("programming","gram") != NULL) << "\n";
 { char s[20]; strcpy(s,"Hi"); strcat(s,"!!"); cout << s << "\n"; }
 cout << "atoi: " << atoi("42") << " " << atof("2.5") << " " << atol("123") << "\n";
 cout << "math: " << pow(2,3) << " " << sqrt(25) << " " << abs(-7) << "\n";
 { int m=612; addVal(m); cout << "byval: " << m << " "; addRef(m); cout << "byref: " << m << "\n"; }
 cout << "static: "; for(int i=0;i<10;i++) showVar(); cout << "\n";
 cout << "nonstatic: "; for(int i=0;i<3;i++) showVar2(); cout << "\n";
 cout << "global0: " << gx << " shadow: "; shadow(); cout << " " << gy << "\n";
 cout << "getSum: " << getSum(5) << " " << getSum(5,2) << " " << getSum(5,2,1) << "\n";
 cout << "sum: " << sum(3,4) << " isEven: " << isEven(6) << isEven(7) << "\n";
 cout << "overload: "; dims(1); dims(1,2); dims(1,2.5); dims(1.5,2.5); cout << "\n";
 cout << "prec2: " << (3 + 4 > 6 && 2 == 2) << " " << (!0 + 1) << "\n";
 return 0;
}
int sum(int a, int b){ return a + b; }
