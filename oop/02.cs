using System;

class Program
{
    static void Main()
    {
        int i = 1;
        int x = 1;
        int sum = 0;

        while (x < 4000000)
        {
            if (x % 2 == 0)
            {
                sum += x;
            }

            int next = i + x;
            i = x;
            x = next;
        }

        Console.WriteLine(sum);
    }
}