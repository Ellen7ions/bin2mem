import os, sys
import json


class Config:
    def __init__(self, config_path='./config.json'):
        super(Config, self).__init__()
        self.config_path = config_path
        self.bin2mem_path = None

        self.init_configs(json.load(open(config_path)))

    def init_configs(self, json_data):
        self.bin2mem_path = json_data['bin2mem.path']
        Config.check_file_exists(self.bin2mem_path)

    @staticmethod
    def check_file_exists(file_name):
        if not os.path.exists(file_name):
            raise Exception(f'{file_name} not found!')


class Convert:
    def __init__(self):
        super(Convert, self).__init__()
        self.config = Config()

        self.FLAG_SAVE_FILES = False
        self.FLAG_FILE_NAME = ''
        self.FLAG_CLEAN_ALL = False

        self.workspace_name = ''
        self.file_name = ''

        self.o_file_path = ''
        self.bin_file_path = ''
        self.coe_file_path = ''

        self.init_flags()
        self.make_workspace()
        self.set_files_path()

    def init_flags(self):
        for i in sys.argv:
            if i == '-s':
                self.FLAG_SAVE_FILES = True
            if i.endswith('.s'):
                self.FLAG_FILE_NAME = i
            if i == 'clean':
                self.FLAG_CLEAN_ALL = True
        if self.FLAG_FILE_NAME == '':
            if os.path.exists('main.s'):
                self.FLAG_FILE_NAME = 'main.s'
            else:
                raise Exception('Where is your input file :(')
        self.workspace_name = self.FLAG_FILE_NAME[:-2]
        self.file_name = self.FLAG_FILE_NAME[:-2]

    def make_workspace(self):
        if not os.path.exists(self.workspace_name):
            os.mkdir(self.workspace_name)

    def set_files_path(self):
        self.o_file_path = f'.\\{self.workspace_name}\\{self.file_name}.o'
        self.bin_file_path = f'.\\{self.workspace_name}\\{self.file_name}.bin'
        self.coe_file_path = f'.\\{self.workspace_name}\\{self.file_name}.txt'

    def mips_gcc_c(self):
        os.system(f'mips-sde-elf-gcc -c {self.FLAG_FILE_NAME} -o {self.o_file_path}')

    def mips_objcopy(self):
        os.system(f'mips-sde-elf-objcopy -O binary {self.o_file_path} {self.bin_file_path}')

    def mips_bin2mem(self):
        os.system(f'{self.config.bin2mem_path} {self.bin_file_path} > {self.coe_file_path}')

    def clean_process_files(self):
        try:
            Config.check_file_exists(self.o_file_path)
            os.system(f'del {self.o_file_path}')
        except Exception as e:
            pass

        try:
            Config.check_file_exists(self.bin_file_path)
            os.system(f'del {self.bin_file_path}')
        except Exception as e:
            pass

        try:
            Config.check_file_exists(self.coe_file_path)
            os.system(f'del {self.coe_file_path}')
        except Exception as e:
            pass

    def run(self):
        self.mips_gcc_c()
        self.mips_objcopy()
        self.mips_bin2mem()

    def clean(self):
        self.clean_process_files()
        os.removedirs(self.workspace_name)

    def mips_objdump(self):
        if os.path.exists(self.o_file_path):
            os.system(f'mips-sde-elf-objdump -d {self.o_file_path}')

    def apply(self):
        if self.FLAG_CLEAN_ALL:
            self.clean()
            return
        self.run()
        if not self.FLAG_SAVE_FILES:
            self.clean_process_files()
            return
        self.mips_objdump()


if __name__ == '__main__':
    c = Convert()
    c.apply()
    # c.mips_gcc_c()
    # c.mips_objcopy()
    # c.mips_bin2mem()
    # config = Config()
