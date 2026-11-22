#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;
double half(int n){ return n / 2; }
void addOne(int n){ n++; }
int main(){
 cout << "010+1=" << 010 + 1 << " 012=" << 012 << "\n";
 { int s=7384; cout << s/3600 << " h " << (s%3600)/60 << " min " << s%60 << " s\n"; }
 { int x=4; x -= 2*3; cout << "x-=" << x << "\n"; }
 { int a=3; int b=a++*2; cout << "a=" << a << " b=" << b << "\n"; }
 cout << 2.0/3 << " " << 17/5 << " " << 10.0/3 << " " << (3>2) << "\n";
 { int x = 9.8; cout << "int9.8=" << x << " 3725%60=" << 3725%60 << "\n"; }
 { int n=4; if (n%2==0) cout << "even "; else cout << "odd "; cout << "done\n"; }
 { int age=15; if (age>=18) cout << "Adult "; cout << "Can vote\n"; }
 { int x=3; if ((x = 7)) cout << x; cout << "\n"; }
 { int a=1,b=2; cout << "["; if(a>3) { if(b>3) cout<<"X"; else cout<<"Y"; } cout << "]\n"; }
 { int m=45; cout << (m >= 50 ? "Pass" : "Fail") << " "; int n=0; cout << ((n>0)?1:-1) << "\n"; }
 { int c=0; for(int i=0;i<10;i+=3) c++; cout << "iters=" << c << "\n"; }
 { int c=0; for (int i = 0; i < 5; i++); c++; cout << "stars=" << c << "\n"; }
 { int c=0; for(int i=0;i<2;i++) for(int j=0;j<3;j++) c++; cout << "#=" << c << "\n"; }
 for (int i=1;i<=10;i++) if (i==5) cout << 3 << " x " << i << " = " << 3*i << "\n";
 cout << ceil(4.01) << " " << half(5) << " " << atof("2.5kg") << "\n";
 { int a=5,b=2; double c=a/b; cout << c << " "; int a9=9; cout << a9/2 << a9%2 << "\n"; }
 { int n=3; switch(n){ case 3: cout<<"three "; case 4: cout<<"four "; default: cout<<"other"; } cout << "\n"; }
 { int x=1; if (x == 5); x++; cout << "x=" << x << "\n"; }
 { int k=9; addOne(k); cout << k << "\n"; }
 { int a=4,b=9; cout << (a<b) << " " << (a==b) << " " << ((5>3)||(2>8)) << "\n"; }
 cout << "A" << "B" << endl << "C" << "\n";
 cout << rand()%100+1 << "\n";
}
