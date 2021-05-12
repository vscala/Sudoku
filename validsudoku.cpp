#define u16 unsigned short
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        u16 seen[3][9] = {0};
        for (int i = 0; i < 81; i++) {
            u16 cur = board[i/9][i%9];
            if (cur == '.') continue;
            cur = (u16)(1 << int(cur-48));
            if (cur & seen[0][i/9]) return false;
            seen[0][i/9] |= (cur);
            if (cur & seen[1][i%9]) return false;
            seen[1][i%9] |= (cur);
            if (cur & seen[2][(i%9)/3 + (i/27)*3]) return false;
            seen[2][(i%9)/3 + (i/27)*3] |= (cur);
        }
        return true;
    }
};
