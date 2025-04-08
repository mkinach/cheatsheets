# C Cheatsheet
#### References:

    TEACH YOURSELF C IN 24 HOURS (2nd Edition)
    Tony Zhang
    Sams 2000

#### Index:

[Text Handling](#text-handling)<br>
[Control Structures](#control-structures)<br>
[Functions](#functions)<br>
[Pointers and Arrays](#pointers-and-arrays)<br>
[Scope and Storage Classes](#scope-and-storage-classes)<br>
[Miscellaneous](#miscellaneous)<br>

---

### Text Handling

Format specifiers
```
%c                Character
%d                Signed integer
%e or %E          Scientific notation of floats
%f                Float
%g or %G          Similar to %e or %E
%hi               Signed integer (short)
%hu               Unsigned Integer (short)
%i                Unsigned integer
%l or %ld or %li  Long
%lf               Double
%Lf               Long double
%lu               Unsigned int or unsigned long
%lli or %lld      Long long
%llu              Unsigned long long
%o                Octal representation
%p                Pointer
%s                String
%u                Unsigned int
%x or %X          Hexadecimal representation
%n                Prints nothing
%%                Prints % character
```

Initializing character constants and strings
```c
#include <stdio.h>
#include <string.h>

int main()
{
  // character constants
  char x = 'a';  // note the single quotes
  char y = 97;   // equivalent to x

  // strings
  char char_str[]   = {'H', 'e', 'l', 'l', 'o', '\0'};  // manually null-terminated (treated as string)
  char char_array[] = {'H', 'e', 'l', 'l', 'o'};        // not null-terminated (not treated as string)
  char str[] = "Hello";                                 // automatically null-terminated (treated as string)

  // note that character constants use '' while strings use ""
  char ch = 'x';        // 1 byte
  char ch_str[] = "x";  // 2 bytes (due to null character)

  // strings are really arrays, so they are really just char pointers
  char *ptr_str;
  ptr_str = "Hello";

  // get the length of a string
  printf("The length of ptr_str is: %d bytes\n", strlen(ptr_str));  // 5 bytes

  // copy a string
  char str1[] = "String content";
  char str2[14];
  strcpy(str2, str1);

  return 0;
}
```

Read a character from stdin with `getc`
```c
#include <stdio.h>

int main()
{
  int ch1, ch2;

  printf("Please type in two characters together:\n");
  ch1 = getc(stdin);
  ch2 = getchar();  // equivalent to getc(stdin)
  printf("The first character you just entered is: %c\n",  ch1);
  printf("The second character you just entered is: %c\n", ch2);

  return 0;
 }
```

Write a character to stdout with `putc`
```c
#include <stdio.h>

int main()
{
  int ch=65;  // numeric value of A in ASCII

  printf("The character that has numeric value of 65 is:\n");
  putc(ch, stdout);  // A
  putchar(ch);  // equivalent to putc(ch, stdout)

  return 0;
}
```

Read/write a string to stdin/stdout with `fgets` and `fputs`
```c
#include <stdio.h>
#include <string.h>

int main()
{
    char str[80];
    int i;

    printf("Enter a string less than 80 characters:\n");
    fgets(str, sizeof(str), stdin); // use fgets to read input
    fputs(str, stdout);             // use fputs to print output

    return 0;
}
```

Align output
```c
#include <stdio.h>

int main()
{
  int num1, num2;
  double num3;

  num1 = 12;
  num2 = 12345;
  num3 = 123.456789;
  printf("%5d\n",  num1);  // pad with spaces (   12)
  printf("%05d\n", num1);  // pad with zeroes (00012)
  printf("%-5d\n", num1);  // left-align      (12   )
  printf("%2d\n",  num2);  // set minimum field width (12345)

  printf("%2.8d\n", num1); // with precision specifier (00000012)
  printf("%9.2f\n", num3); // with precision specifier (   123.46)

  return 0;
}
```

Read from stdin with `scanf`
```c
#include <stdio.h>

int main() {
  char str[80];
  int x, y;
  float z;

  printf("Enter two integers separated by a space:\n");
  if (scanf("%d %d", &x, &y) != 2) {
    printf("Invalid input for integers.\n");
    return 1;
  }

  printf("Enter a floating-point number:\n");
  if (scanf("%f", &z) != 1) {
    printf("Invalid input for floating-point number.\n");
    return 1;
  }

  // consume the newline character left in the input buffer
  while (getchar() != '\n');

  printf("Enter a string (up to 79 characters):\n");
  if (scanf("%79s", str) != 1) {
    printf("Invalid input for string.\n");
    return 1;
}

printf("Here is what you've entered:\n");
printf("%d %d\n%f\n%s\n", x, y, z, str);

return 0;
}
```

### Control Structures

`while` loops
```c
#include <stdio.h>

int main() {
  int i = 1;

  while (i <= 5) {
    if (i == 3) break;
    printf("%d\n", i);
    i++;
  }

  while (i <= 10) {
    if (i == 8) { i++; continue; }  // skip iteration
    printf("%d\n", i);
    i++;
  }

  return 0;
}

```

`do-while` loops
```c
#include <stdio.h>

int main()
{
  int i = 65;

  do {
    printf(“The numeric value of %c is %d.\n”, i, i);
    i++;
  } while (i<72);

  return 0;
}
```

`for` loops
```c
#include <stdio.h>

int main()
{
  int i, j;

  printf("Hex(uppercase) Hex(lowercase) Decimal\n");
  for (i=0; i<16; i++){
    printf("%X %x %d\n", i, i, i);
  }

  for (i=0; i<8; i++);  // a null statement

  for (i=0, j=8; i<8; i++, j--){  // more complicated now
    printf(“%d + %d = %d\n”, i, j, i+j);
  }

  return 0;
}
```

`if` statements
```c
#include <stdio.h>

int main() {
  int number = 10;

  if (number > 10)  // braces not needed for one-liners
    printf("Number is greater than 10.\n");
  else if (number > 5)
    printf("Number is greater than 5 but not greater than 10.\n");
  else
    printf("Number is not greater than 5.\n");

  return 0;
}
```

Conditional operators
```c
#include <stdio.h>

int main() {
  int num1 = 10;
  int num2 = 20;

  // test condition ? pass : fail;
  int max = (num1 > num2) ? num1 : num2;

  printf("The maximum value is: %d\n", max);

  return 0;
}
```

`switch` statements
```c
#include <stdio.h>

int main() {
  int choice = 1;

  switch (choice) {
    case 1:
        printf("Option 1\n");
        break;  // needed, or else "Option 2" will be printed
    case 2:
        printf("Option 2\n");
        break;
    default:
        printf("Invalid choice\n");
  }

  return 0;
}
```

### Scope and Storage Classes

Scope hierarchy
```
program scope > file scope > function scope > block scope
```

Block scope
```c
#include <stdio.h>

int main() {
  int x = 5;  // outer scope

  printf("Outer x: %d\n", x);  // 5

  {
    int x = 10; // inner scope
    printf("Inner x: %d\n", x);  // 10
  }

  printf("Outer x: %d\n", x);  // 5

  return 0;
}
```

Function scope, file scope and program scope
```c
#include <stdio.h>

// program scope and file scope variables retains their value throughout the program
int x = 1234;         // program scope (external linkage; accessible from other source files)
double y = 1.234567;  // program scope
static int z = 5678;  // file scope (internal linkage; accessible only from current file)

void function_1()
{
  // no block scope, so defaults to program/file scope
  printf("From function_1:\n x=%d, y=%f\n", x, y);
}

int main()
{
  int x = 4321;  // block scope in main

  function_1();  // x=1234, y=1.234567
  printf("Within the main block:\n x=%d, y=%f\n", x, y);  // x=4321, y=1.234567

  {
    double y = 7.654321; // block scope within the nested block
    function_1();  // x=1234, y=1.234567
    printf("Within the nested block:\n x=%d, y=%f\n", x, y);  // x=4321, y=7.654321
  }

  return 0;
}
```

The `extern` keyword
```c
#include <stdio.h>

// declare a variable which was already defined with program scope in another file
extern int x;

int main() {
  printf("Shared variable: %d\n", x);
  return 0;
}
```

Storage class specifiers
```c
#include <stdio.h>

// 'auto' variables are created and destroyed during each function call
void autoExample() {
  int x = 5;
  printf("Inside autoExample: x = %d\n", x);
}

void staticExample() {
  static int y = 10;  // 'y' retains its value between function calls
  y++;
  printf("Inside staticExample: y = %d\n", y);
}

int main() {
  autoExample();  // x = 5
  auto int a = 7; // 'auto' is the default and therefore optional (rarely explicitly declared)
  printf("Inside main: a = %d\n", a);  // a = 7

  staticExample();  // y = 11
  staticExample();  // y = 12
  return 0;
}
```

### Functions

Basic function usage
```c
#include <stdio.h>
#include <stdarg.h>  // needed for functions that take variable number of arguments

// function with no arguments
void func_noargs() {
  printf("This function takes no arguments.\n");
}

// function with a fixed number of arguments
void func_fixedargs(int a, int b) {
  printf("This function takes two arguments: %d and %d\n", a, b);
}

// function with a variable number of arguments
void func_varargs(int num, ...) {

  // custom array data type (defined in stdarg.h) needed for va_*()
  va_list args;

  // initialize the va_list variable to point to the first argument (out of num total)
  va_start(args, num);

  printf("This function takes %d arguments: ", num);
  for (int i = 0; i < num; i++) {
    int arg = va_arg(args, int);  // retrieve the next argument
    printf("%d ", arg);
  }

  va_end(args);  // perform cleanup operations
}

int main() {
  func_noargs();  // This function takes no arguments.

  func_fixedargs(10, 20);  // This function takes two arguments: 10 and 20

  func_varargs(4, 1, 2, 3, 4);  // This function takes 4 arguments: 1 2 3 4

  return 0;
}
```

### Pointers and Arrays

Declaring and assigning values to pointers
```c
#include <stdio.h>

int main()
{
  char c, *ptr_c;
  int x, *ptr_x;
  float y, *ptr_y;

  printf("c: address=%p, content=%c\n", &c, c);    // c: address=0xa9ef, content=
  printf("x: address=%p, content=%d\n", &x, x);    // x: address=0xa9dc, content=0
  printf("y: address=%p, content=%5.2f\n", &y, y); // y: address=0xa9cc, content= 0.00

  c = 'A';
  x = 7;
  y = 123.45;
  printf("c: address=%p, content=%c\n", &c, c);    // c: address=0xa9ef, content=A
  printf("x: address=%p, content=%d\n", &x, x);    // x: address=0xa9dc, content=7
  printf("y: address=%p, content=%5.2f\n", &y, y); // y: address=0xa9cc, content=123.45

  ptr_c = &c;
  printf("ptr_c: address=%p, content=%p\n", &ptr_c, ptr_c);  // ptr_c: address=0xa9e0, content=0xa9ef
  printf("*ptr_c => %c\n", *ptr_c);  // *ptr_c => A

  ptr_x = &x;
  printf("ptr_x: address=%p, content=%p\n", &ptr_x, ptr_x);  // ptr_x: address=0xa9d0, content=0xa9dc
  printf("*ptr_x => %d\n", *ptr_x);  // *ptr_x => 7

  ptr_y = &y;
  printf("ptr_y: address=%p, content=%p\n", &ptr_y, ptr_y);  //ptr_y: address=0xa9c0, content=0xa9cc
  printf("*ptr_y => %5.2f\n", *ptr_y);  // *ptr_y => 123.45

  return 0;
}
```

Update variable values via pointers
```c
#include <stdio.h>

int main()
{
  char c, *ptr_c;

  c = 'A';
  printf("c: address=%p, content=%c\n", &c, c);              // c: address=0x33ff, content=A
  ptr_c = &c;
  printf("ptr_c: address=%p, content=%p\n", &ptr_c, ptr_c);  // ptr_c: address=0x33f0, content=0x33ff
  printf("*ptr_c => %c\n", *ptr_c);                          // *ptr_c => A
  *ptr_c = 'B';
  printf("ptr_c: address=%p, content=%p\n", &ptr_c, ptr_c);  // ptr_c: address=0x33f0, content=0x33ff
  printf("*ptr_c => %c\n", *ptr_c);                          // *ptr_c => B

  printf("c: address=%p, content=%c\n", &c, c);              // c: address=0x33ff, content=B

  return 0;
}
```

Initializing arrays
```c
#include <stdio.h>

int main() {
  int numbers1[5] = {1, 2, 3, 4, 5};  // initialize with specific size
  int numbers2[]  = {1, 2, 3, 4, 5};  // initialize with inferred size

  char hello[] = "Hello";  //initialize character array with a string literal

  int twodim[3][5] = {  // multidimensional array [rows][columns]
    {1, 2, 3, 4, 5},
    {10, 20, 30, 40, 50},
    {100, 200, 300, 400, 500}
  };

  // unsized arrays
  int list_int[] = {10, 20, 30, 40, 50, 60, 70, 80, 90};
  char list_ch[][2] = {  // in multidimensional case, you have to specify
    ‘a’, ‘A’,            // all but the first dimension size
    ‘b’, ‘B’,
    ‘c’, ‘C’,
    ‘d’, ‘D’,
    ‘e’, ‘E’,
    ‘f’, ‘F’,
    ‘g’, ‘G’};

  int test[2];
  test[1] = 7;
  printf("%d ", test[1]);  // 7
  printf("%d ", test[2]);  // uninitialized; output will be garbage

  return 0;
}
```

Computing the size of an array
```c
#include <stdio.h>

int main() {
  int total_byte;
  int list_int[10];

  total_byte = sizeof(int) * 10;
  printf("The size of int is %d bytes.\n", sizeof(int));  // 4
  printf("The array of 10 ints has a total of %d bytes.\n", total_byte);  // 40

  // expect 40-4=36 bytes of memory usage (since it counts to beginning of last element)
  printf("The address of the first element: %p\n", &list_int[0]);  // 0x2320
  printf("The address of the last element: %p\n",  &list_int[9]);  // 0x2344 = 36 bytes ahead

  return 0;
}
```

Referencing an array with a pointer
```c
#include <stdio.h>

int main() {
  int *ptr_int;
  int list_int[10];
  int i;

  // fill the array
  for (i = 0; i < 10; i++) list_int[i] = i + 1;

  // assign address of first element of array to the pointer
  ptr_int = list_int;
  printf("The start address of the array: %p\n",  ptr_int);  // 0x2bc0
  printf("The value of the first element: %d\n", *ptr_int);  // 1

  // another way
  ptr_int = &list_int[0];
  printf("The address of the first element: %p\n", ptr_int); // 0x2bc0
  printf("The value of the first element: %d\n",  *ptr_int); // 1

  return 0;
}
```

Printing an array of characters
```c
#include <stdio.h>

int main()
{
  // note: the null character (\0) automatically terminates the string
  char array_ch[7] = {'H', 'e', 'l', '\0', 'l', 'o', '!'};
  int i;

  for (i = 0; i < 7; i++)
    printf("array_ch[%d] contains: %c\n", i, array_ch[i]);
    // array_ch[0] contains: H
    // array_ch[1] contains: e
    // array_ch[2] contains: l
    // array_ch[3] contains:
    // array_ch[4] contains: l
    // array_ch[5] contains: o
    // array_ch[6] contains: !

  // print characters by fetching individual elements
  for (i = 0; array_ch[i] != '\0' && i < 7; i++)
    printf("%c", array_ch[i]);  // Hel

  // print characters by accessing address of first element
  printf("%s\n", array_ch);  // Hel

  return 0;
}
```

Multidimensional arrays
```c
#include <stdio.h>

int main()
{
  int two_dim[3][5] = {
    {1, 2, 3, 4, 5},
    {10, 20, 30, 40, 50},
    {100, 200, 300, 400, 500}
  };

  for (int i = 0; i < 3; i++)
  {
    printf("\n");
    for (int j = 0; j < 5; j++)
      printf("%6d", two_dim[i][j]);
  }

  return 0;
}
```

### Miscellaneous

Include directives
```c
#include <stdio.h>  // include from system locations
#include "mylib.h"  // include from local directory
```

Pre-increment and post-increment operators
```c
#include <stdio.h>

int main()
{
  int w, x, y, z, result;

  w = x = y = z = 1;

  // pre-increment increments, but returns incremented value
  // post-increment increments, but returns unincremented value
  result = ++w;  // result is now 2, w is now 2
  result = x++;  // result is now 1, x is now 2
  result = --y;  // result is now 0, y is now 0
  result = z--;  // result is now 1, z is now 0

  return 0;
}
```

`sizeof` operator
```c
#include <stdio.h>

int main()
{
  char ch = ' ';
  int int_num = 0;
  float flt_num = 0.0f;
  double dbl_num = 0.0;

  printf("The size of char is: %d-byte\n", sizeof(char));       // 1-byte
  printf("The size of ch is: %d-byte\n", sizeof ch );           // 1-byte
  printf("The size of int is: %d-byte\n", sizeof(int));         // 4-bytes
  printf("The size of int_num is: %d-byte\n", sizeof int_num);  // 4-bytes
  printf("The size of float is: %d-byte\n", sizeof(float));     // 4-bytes
  printf("The size of flt_num is: %d-byte\n", sizeof flt_num);  // 4-bytes
  printf("The size of double is: %d-byte\n", sizeof(double));   // 8-bytes
  printf("The size of dbl_num is: %d-byte\n", sizeof dbl_num);  // 8-bytes

  return 0;
}
```

Bitwise operators
```
&   bitwise AND
|   bitwise OR
^   bitwise XOR
~   bitwise complement
>>  right-shift operator (div by 2)
<<  left-shift operator (mult by 2)
```

```c
#include <stdio.h>

int main() {
  int num1 = 12;  // 0b1100
  int num2 = 7;   // 0b0111

  int result_and = num1 & num2;  // bitwise AND
  int result_or = num1 | num2;   // bitwise OR
  int result_xor = num1 ^ num2;  // bitwise XOR
  int result_shift = num1 >> 2;  // bitwise shift right

  printf("Bitwise AND: %d\n", result_and);            // 4
  printf("Bitwise OR: %d\n",  result_or);             // 15
  printf("Bitwise XOR: %d\n", result_xor);            // 11
  printf("Bitwise shift right: %d\n", result_shift);  // 3

  return 0;
}
```

Basic data modifiers
```c
#include <stdio.h>
#include <limits.h>

int main() {
  // note: unsigned modifier is meaningful only to the integer data types: char, int
  signed int signedIntMax = INT_MAX;
  unsigned int unsignedIntMax = UINT_MAX;
  short int shortIntMax = SHRT_MAX;
  unsigned short int unsignedShortIntMax = USHRT_MAX;
  long int longIntMax = LONG_MAX;
  unsigned long int unsignedLongIntMax = ULONG_MAX;

  // alternate declarations
  unsigned int a; // equivalent to 'unsigned int a'
  unsigned b;     // equivalent to 'unsigned int b'
  int c = 12345u; // equivalent to 'unsigned int c = 12345'
  short x;        // equivalent to 'signed short int x'
  int y = 12345l; // equivalent to 'signed long int y'

  // note: may be compiler-dependent
  printf("Max signed int: %d\n", signedIntMax);                 // 2147483647
  printf("Max unsigned int: %u\n", unsignedIntMax);             // 4294967295
  printf("Max signed short int: %d\n", shortIntMax);            // 32767
  printf("Max unsigned short int: %u\n", unsignedShortIntMax);  // 65535
  printf("Max signed long int: %ld\n", longIntMax);             // 9223372036854775807
  printf("Max unsigned long int: %lu\n", unsignedLongIntMax);   // 18446744073709551615

  printf("The size of short int is: %d.\n",   sizeof(short int));    // 2
  printf("The size of long int is: %d.\n",    sizeof(long int));     // 8
  printf("The size of float is: %d.\n",       sizeof(float));        // 4
  printf("The size of double is: %d.\n",      sizeof(double));       // 8
  printf("The size of long double is: %d.\n", sizeof(long double));  // 16

  return 0;
}
```

`const` modifier
```c
#include <stdio.h>

int main() {
  // const variables cannot be changed...
  const double circle_ratio = 3.141593;
  const char str[] = "A string constant";

  // ...so this would be illegal
  //str[0] = 'a';

  // the object pointed to by this pointer cannot change...
  char const *ptr_str = "A string constant";

  // ...so this would be illegal
  //*ptr_str = 'a';

  return 0;
}
```
