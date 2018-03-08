#include <iostream>
#include <string>
#include "diff_match_patch.h"

using namespace std;

int main(int argc, char **argv) {
    diff_match_patch<string> dmp;
    auto diffs = dmp.diff_main("Good dog", "Bad dog");
    auto patches = dmp.patch_make(diffs);
    cout << dmp.patch_toText(patches) << "\n";
    return 0;
}
