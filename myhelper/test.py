from .wasm.wasm.decode import decode_bytecode, decode_module
from math import *
from .wasm.wasm.formatter import format_instruction

from .wasm.wasm.modtypes import DataSection

def initDataSec(file):
	dataSec = {}

	with open(file, 'rb') as raw:
		raw = raw.read()

	mod_iter = iter(decode_module(raw))
	header, header_data = next(mod_iter)

	for cur_sec, cur_sec_data in mod_iter:
		if isinstance(cur_sec_data.get_decoder_meta()['types']['payload'], DataSection):
			for idx, entry in enumerate(cur_sec_data.payload.entries):
				# print(idx, str(entry.data.tobytes(), 'utf-8'))
				for cur_insn in decode_bytecode(entry.offset):
					op = format_instruction(cur_insn)
					if op.split(" ")[0] == "i32.const":
						dataSec[op.split(" ")[1]] = entry.data.tobytes()

	return dataSec



