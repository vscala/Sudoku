class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        long seen[9] = {0};
        for (int i = 0; i < 81; i++) {
            long cur = board[i/9][i%9];
            if (cur == '.') continue;
            cur = long(1 << (cur-'0'));
            if (cur & seen[i/9] || (cur << 9) & seen[i%9] || (cur << 18) & seen[(i%9)/3 + (i/27)*3]) return false;
            seen[i/9] |= (cur);
            seen[i%9] |= (cur << 9);
            seen[(i%9)/3 + (i/27)*3] |= (cur << 18);
        }
        return true;
    }
};
