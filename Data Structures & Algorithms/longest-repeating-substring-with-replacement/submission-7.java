class Solution {
    public int characterReplacement(String s, int k) {
    int l=0;
    int max=0;
    Map<Character,Integer> mapper = new HashMap<>();
    for (int r =0;r<s.length();r++){
        if (mapper.containsKey(s.charAt(r))){
            mapper.put(s.charAt(r),mapper.get(s.charAt(r))+1);
        }
        else{
            mapper.put(s.charAt(r),1);
        }
        if((r-l+1)-Collections.max(mapper.values())<=k){
            max=Math.max(max,r-l+1);
        }
        else{
            mapper.put(s.charAt(l),mapper.get(s.charAt(l))-1);
            l+=1;
        }

    }
    return max;
    }
}
