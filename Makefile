CONTIKI_PROJECT = aes
all: $(CONTIKI_PROJECT)

# Add library flags
# TARGET_LIBFILES += -lm

# Add project modules
MODULES += os/services/simple-energest

CONTIKI = ../..
include $(CONTIKI)/Makefile.include