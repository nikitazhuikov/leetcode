class Solution {
    fun removeAnagrams(words: Array<String>): List<String> {
        val result = words.toMutableList()
        var i = 1
        while (i < result.size) {
            if (areAnagrams(result[i], result[i - 1])) {
                result.removeAt(i)
            } else {
                i++
            }
        }
        return result
    }

    private fun areAnagrams(s1: String, s2: String): Boolean {
        if (s1.length != s2.length) return false
        val counts = IntArray(26)
        for (i in s1.indices) {
            counts[s1[i] - 'a']++
            counts[s2[i] - 'a']--
        }
        return counts.all { it == 0 }
    }
}