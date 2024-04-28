package LeetCodes;

public class LongestCommonPrefix {
    public static void main(String[] args) {
        String[] s = {"abc"};
        String word = longestCommonPrefix(s);
        System.out.println(word);
    }
    public static String longestCommonPrefix(String[] s){
        String ans = "";
        if(s[0].length() == 0)
            return "";
        
            for (int i = 0; i < s[0].length(); i++) {
                ans += s[0].charAt(i); // add the first strings char

                for(int j = 1; j < s.length; j++){ // start at the next string in the array and see if all of them have this first letter
                    if(s[j].length()-1<i){return ans.substring(0,i);} // if the strings are all not the same length
                    if(s[j].length() == 0){return "";} // edge case
                    if(s[j].charAt(i)==(ans.charAt(i))){ // check to see if all the strings in the array have that same letter as the first one
                        continue;
                    }else{
                        return ans.substring(0, i); // because it prematurally adds the intail strings next char so u have to cut it short
                    }

                }

            }
        return ans;
    }
}
