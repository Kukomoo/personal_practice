#include <stdio.h>
#include <stdlib.h>

int main()
{
	char opreator;
	double num1;
	double num2;

	printf("Enter 1st number: ");
	scanf("%lf", &num1);
	printf("Enter operator of choice: ");
	scanf(" %c", &opereator);
	printf("Enter 2nd number: ");
	scanf("%lf", &num2);

	if(opreator == '+')
	{ printf("%f", num1 + num2); }
	else if(opreator == '-')
	{ printf("%f", num1 - num2); }
	else if(opreator == '/')
	{ printf("%f", num1 / num2); }
	else if(opreator == '*')
	{ printf("%f", num1 * num2); }
	else { printf("Invalid operator")}
}
