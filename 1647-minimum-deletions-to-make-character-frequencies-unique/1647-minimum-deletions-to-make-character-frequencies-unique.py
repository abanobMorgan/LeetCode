class Solution:
    def minDeletions(self, s: str) -> int:
        # Store the frequency of each character
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        frequency.sort(reverse=True)

        delete_count = 0
        # Maximum frequency the current character can have
        max_freq_allowed = int(frequency[0])
        # Iterate over the frequencies in descending order
        for freq in range(len(frequency)):
            # Delete characters to make the frequency equal the maximum frequency allowed
            if frequency[freq] > max_freq_allowed:
                delete_count += frequency[freq] - max_freq_allowed
                frequency[freq] = max_freq_allowed

            
            if frequency[freq] == 0 :
                delete_count += sum(frequency[freq:])
                return delete_count
            # Update the maximum allowed frequency
            max_freq_allowed = max(0, frequency[freq] - 1)
            
        return delete_count