class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap<Character,Integer> first=new HashMap<>();
        HashMap<Character,Integer> second=new HashMap<>();
        for(Integer i=0;i<s.length();i++){
            if (first.containsKey(s.charAt(i))){
                first.put(s.charAt(i),first.get(s.charAt(i))+1);
            }
            else{
                first.put(s.charAt(i),1);
            }
            if (second.containsKey(t.charAt(i))){
                second.put(t.charAt(i),second.get(t.charAt(i))+1);
            }
            else{
                second.put(t.charAt(i),1);
            }
        }
        if(second.equals(first)){
            return true;
        }
        else{
            return false;
        }
        
    }
}
