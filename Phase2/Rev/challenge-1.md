# Challenge 1
## Challenge Description
```
CAN YOU FIGURE OUT THE HIDDEN FLAG WITHIN THE BINARY!?
```
## <span style="color:aqua;">Analysis</span>
We were provided an executable file named **Tryme**. After granting the permission to the file I found out that the file requests a flag and we have to find the correct flag.
<br>So I used an reversing tool called ghidra and opened the project with the "Tryme" file.
<br>
After opening the assembly language I found the main function where all the code was located 
```

undefined8 main(int param_1,long param_2)

{
  undefined8 uVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  int local_98;
  int local_94;
  int local_88 [24];
  byte abStack_28 [24];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 == 1) {
    puts("Usage: ./crackme FLAG");
    uVar1 = 1;
  }
  else {
    sVar2 = strlen(*(char **)(param_2 + 8));
    if (sVar2 == 0x15) {
      for (local_98 = 0; local_98 < 0x15; local_98 = local_98 + 1) {
        abStack_28[local_98] = "sup3r_s3cr3t_k3y_1337"[local_98] - 0x22;
      }
      local_88[0] = 0x37;
      local_88[1] = 0x3f;
      local_88[2] = 0x2f;
      local_88[3] = 0x76;
      local_88[4] = 0x2b;
      local_88[5] = 0x62;
      local_88[6] = 0x28;
      local_88[7] = 0x21;
      local_88[8] = 0x34;
      local_88[9] = 0xf;
      local_88[10] = 0x77;
      local_88[11] = 0x62;
      local_88[12] = 0x48;
      local_88[13] = 0x27;
      local_88[14] = 0x75;
      local_88[15] = 8;
      local_88[16] = 0x56;
      local_88[17] = 0x6a;
      local_88[18] = 0x68;
      local_88[19] = 0x4e;
      local_88[20] = 0x68;
      for (local_94 = 0; local_94 < 0x15; local_94 = local_94 + 1) {
        if ((int)(char)(abStack_28[local_94] ^ *(byte *)((long)local_94 + *(long *)(param_2 + 8)))
            != local_88[local_94]) {
          puts("Wrong flag");
          uVar1 = 1;
          goto LAB_00101355;
        }
      }
      printf("You found a flag! %s\n",*(undefined8 *)(param_2 + 8));
      uVar1 = 0;
    }
    else {
      puts("Wrong flag");
      uVar1 = 1;
    }
  }
LAB_00101355:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar1;
}

```
After analyzing the code I found out that there was an xor operation between two variables. And the resulted Output was compared to the user input. At first the code check whether the input is 0x15 or 21 cahracter long or not.Then the variable abStack_28[local_98] was assigned the long string **"sup3r_s3cr3t_k3y_1337"** and __0x22__ value was reduced from its ASCII value.
Another variable was **local_88** whose each character was assigned manually in hexadecimal value.
After a bit of rev-ing i figured out the flag:

## <span style="color:Green;">Flag- flag{_y0u_f0und_key_}</span>