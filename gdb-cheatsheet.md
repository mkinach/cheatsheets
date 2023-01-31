# GDB Cheatsheet
#### References:

    [1] http://cs.baylor.edu/~donahoo/tools/gdb/tutorial.html
    [2] http://web.mit.edu/gnu/doc/html/gdb_toc.html
    [3] https://www.open-mpi.org/faq/?category=debugging#build-ompi-with-g
    [4] https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html#Debugging-Options
    [5] http://www.brendangregg.com/blog/2016-08-09/gdb-example-ncurses.html

#### Index:

[Basics](#basics)<br>
[Fortran Debugging](#fortran-debugging)<br>
[C Debugging](#c-debugging)<br>
[MPI Debugging](#mpi-debugging)<br>
[Miscellaneous](#miscellaneous)<br>

---

### Basics
Assuming your executable is named `myprog`, start the debugger via
```
$ gdb myprog
```

To set a breakpoint at a specific line in the code
```
(gdb) b 43
(gdb) b main.f:43
(gdb) info breakpoints
```

Run the program
```
(gdb) run
```

Run the program with a command line argument
```
(gdb) run id0
```

Step through the program starting at the breakpoint
```
(gdb) step
```

Step over (instead of into) functions
```
(gdb) next
```

List all (nested) frames with
```
(gdb) backtrace
```

Pick a frame `n` to investigate
```
(gdb) frame n
```

Go up or down a frame
```
(gdb) up
(gdb) down
```

List all (local) variables within a frame
```
(gdb) info locals
```

List all arguments passed to the current frame
```
(gdb) info args
```

Print the value of a variable `myvar` at a specific step within a frame
```
(gdb) print myvar
```

Set the value of a variable `myvar` within the current frame
```
(gdb) set variable myvar=10
```

Get the data type of a variable/symbol
```
(gdb) ptype <var>
(gdb) whatis <var>
```

Print 10 lines around the exception, or around some specific line
```
(gdb) list
(gdb) list <linenum>
```

Look forward or backward in the code
```
(gdb) list 
(gdb) list -
```

Print first `n` bytes from an array:
```
(gdb) print *myarray@n
```

To analyze a core file
```
$ gdb <app> <corefile>
```

### Fortran Debugging
Some useful debug flags (assuming `gfortran` or `mpifort`)
```
# -ggdb: produce debugging info for GDB
# -Wall: verbose warnings at compile time
# -fcheck=bounds: runtime check array bounds
# -ffpe-trap=underflow,denormal,overflow,invalid: stop execution for FPEs
# -finit-real=snan: check uninitialized variables
FDEBUGFLAGS  = -ggdb -fcheck=bounds -ffpe-trap=overflow,invalid,zero -finit-real=snan
#FDEBUGFLAGS := $(FDEBUGFLAGS) -ffpe-trap=underflow,denormal  # usually not a meaningful error
FDEBUGFLAGS := $(FDEBUGFLAGS) -Wall
F77          = mpifort $(FDEBUGFLAGS) -fno-second-underscore
F77_LOAD     = mpifort $(FDEBUGFLAGS) -fno-second-underscore -L/usr/local/lib
```
You should also turn off any optimization flags (e.g. `-O3`). Some other possibly useful debug flags are listed in [4]


### C Debugging
Some useful debug flags (assuming `gcc` or `mpicc`)
```
# -ggdb: produce debugging info for GDB
# -Wall: verbose warnings at compile time
# -Wfloat-equal: warning if floating point numbers are using in equality comparisons
CDEBUGFLAGS  = -ggdb 
CDEBUGFLAGS := $(CDEBUGFLAGS) -Wall -Wfloat-equal
CCFLAGS      = 
CC           = mpicc $(CDEBUGFLAGS)
```

To enable additional core dumps on seg faults, NaNs, over/underflow errors, etc., add the following lines to your code
```
#include <fenv.h>
feenableexcept(FE_DIVBYZERO | FE_INVALID | FE_OVERFLOW);
```

### MPI Debugging

**NOTE**: for more advanced MPI debugging, you probably want to use a dedicated graphical debugger such as Arm DDT. See `PhD-tutorials/MPI` for more information

To debug MPI jobs running locally on only a few processors:
1. Launch a seperate gdb instance for each processor (note that the MPI flag `--oversubscribe` can simulate more processors than may be available on your system)
    ```
    $ mpirun --oversubscribe -np <NP> konsole -e gdb my_mpi_application
    ```

2. If there are input files or arguments to your MPI program, enter the following in all of the gdb windows that launch
    ```
    (gdb) run [arg1] [arg2] ... [argn]
    ```

<br>To debug MPI jobs on a remote cluster with a small number of processors (up to maybe ~8?):
1. Assuming C, insert the following code somewhere in your application where you want the program to wait
    ```
    {   // ALL PROCESSES WILL WAIT HERE UNTIL ATTACHED TO DEBUGGER
        volatile int i = 0;
        char hostname[256];
        gethostname(hostname, sizeof(hostname));
        printf("PID %d on %s ready for attach\n", getpid(), hostname);
        fflush(stdout);
        while (0 == i)
        sleep(5);
    }
    ```

2. Prepare to attach gdb to each process by looking for the nodes where the jobs are running
    ```
    $ squeue -u $USER
    ```

3. SSH into the running nodes (e.g. `ssh user@gra1234`) and attach the gdb process (`<pid>` can be found in the output file of the job)
    ```
    $ gdb --pid <pid> <app>
    ```
  
4. Once in the debugger go to the frame with the above block of code and continue execution with
    ```
    (gdb) set var i = 7
    ```

If you want live execution control, set a breakpoint and continue execution until the breakpoint is hit; then you will have full control.  You can also edit the above code to only pause in specific MPI processes (for example, by only pausing on rank 0, etc.)

**NOTE**: you can add compiler/linker debug flags (such as `-g`) to the Makefile and turn off optimization options (such as by using `-O0`), but you should actively avoid these flags when *building* OpenMPI, since this would lead you to step into internal MPI functions which you probably don't want

### Miscellaneous

If you get errors like
```
(gdb) error reading variable: value requires 1054728 bytes, which is more than max-value-size
```
it is because gdb cannot store values of large arrays. You can fix this by entering at the prompt
```
(gdb) set max-value-size unlimited
```
 
If core dumps are not being output, set soft limits to unlimited on your machine
```
$ ulimit -Sc unlimited
```

To generate a core dump on a hanging process
```
$ gcore <pid>
```
or
```
$ kill -ABRT <pid>
```

You may sometimes get an error like the following:
```
__math_divzero (sign=1) at ../sysdeps/ieee754/dbl-64/math_err.c:70
70      ../sysdeps/ieee754/dbl-64/math_err.c: No such file or directory.
```
You can step over this exception by using the `step` command


