################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

# Each subdirectory must supply rules for building sources it contributes
%.obj: ../%.c $(GEN_OPTS) | $(GEN_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: C6000 Compiler'
	"C:/ti/ccsv8/tools/compiler/ti-cgt-c6000_8.2.4/bin/cl6x" -mv6740 --abi=eabi -g --include_path="C:/Users/alexp/Documents/ECET491/Project Time Machine/OMAP_Programming/TimeMachine2" --include_path="C:/ti/ccsv8/tools/compiler/ti-cgt-c6000_8.2.4/include" --diag_wrap=off --display_error_number --diag_warning=225 --preproc_with_compile --preproc_dependency="$(basename $(<F)).d_raw" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: "$<"'
	@echo ' '

%.obj: ../%.asm $(GEN_OPTS) | $(GEN_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: C6000 Compiler'
	"C:/ti/ccsv8/tools/compiler/ti-cgt-c6000_8.2.4/bin/cl6x" -mv6740 --abi=eabi -g --include_path="C:/Users/alexp/Documents/ECET491/Project Time Machine/OMAP_Programming/TimeMachine2" --include_path="C:/ti/ccsv8/tools/compiler/ti-cgt-c6000_8.2.4/include" --diag_wrap=off --display_error_number --diag_warning=225 --preproc_with_compile --preproc_dependency="$(basename $(<F)).d_raw" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: "$<"'
	@echo ' '


