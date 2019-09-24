function! HelloVim()
python3 << EOF
import sys
sys.path.append(".")
import echo
echo.sayHello()
EOF
endfunction
