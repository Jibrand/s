// 1
//  THe code adds the values on Port B and Port C and Displays on Port D.
int main()
{
    DDRB = 0x00;
    DDRC = 0x00;
    DDRD = 0xFF;

    while (1)
        PORTD = PINC + PINB;
    return 0;
}

// 1

#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 8000000UL

int main()
{
    DDRB = 0xFF;

    while (1)
    {
        POROTB = 0X00;
        _DELAY_US();
        POROTB = 0XFF;
        _DELAY_US();
        return (0);
    }
}

void DELAY()
{
    unassigned int i;
    for (i = 0; i < 50000; i++)
    {
    }
}

// 3
void setup()
{
    DDRB = 0x00; // input
    DDRD = 0xFF; // output

    // TODO: put your setup code here, to run once:
}

void loop()
{
    if (PINB == 0x01)
    {
        // PORTD |= (1<<4);
        PORTD = 0xA0;
    }
    else
    {
        // PORTD &= ~(1<<4);
        PORTD = 0x0A;
    }
}

// fabonaccii
int fabonacci(int n);

int mani()
{
    unassigned sum = 0;

    for (i i = 0; i < 11; i++)
    {
        sum += fabonacci(i);
    }
}



PD0 → 0x01
PD1 → 0x02
PD2 → 0x04
PD3 → 0x08
PD4 → 0x10
PD5 → 0x20
PD6 → 0x40
PD7 → 0x80


#include <avr/io.h>

int main()
{
    DDRC = 0x00;   // PORTC input
    DDRD = 0xFF;   // PORTD output

    while (1)
    {
        if (PINC == 0x20)   // PC5 is HIGH (0x20 = bit 5)
        {
            PORTD = 0xFF;  // Send HIGH to PORTD
        }
        else
        {
            PORTD = 0x00;  // Send LOW to PORTD
        }
    }
}

#include <avr/io.h>

int main()
{
    unsigned char count = 0;

    DDRD = 0x0F;
    DDRC = 0x00;

    while (1)
    {
        if (PINC == 0x20)
        {
            if (count < 9)
                count++;
            PORTD = count;
        }
        else if (PINC == 0x10)
        {
            if (count > 0)
                count--;
            PORTD = count;
        }
    }
}


