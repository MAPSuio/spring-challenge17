import java.util.Scanner;

public class Torenord {
    // True if `s` is a real palindrome as defined by Anna, otherwise false.
    static boolean isRealPalindrome(String s) {
        return s.chars().distinct().count() > 1                     // Contains more
                                                                    // than one letter
            && s.equals(new StringBuilder(s).reverse().toString()); // Is a palindrome
    }

    // Expects the input given to stdin to be a list of words with one word per line.
    // Usage: java Torenord < data.txt
    public static void main(String[] args) {
        int n = 0;              // Number of real palindromes
        String s = "";          // Longest real palindrome

        Scanner sc = new Scanner(System.in, "UTF-8");

        while (sc.hasNextLine()) {
            String word = sc.nextLine();

            if (isRealPalindrome(word)) {
                n += 1;                           // Increment number of palindromes
                if (word.length() > s.length()) {
                    s = word;                     // Update longest palindrome found
                }
            }
        }

        if (!s.equals("")) {
            System.out.println(n + " " + s); // If at least one palindrome has been
                                             // found, give the answer
        }
    }
}
