from parser import parse_stl_mvp

from analysis.basic_blocks import build_basic_blocks, build_block_cfg
from analysis.dataflow import build_use_def
from analysis.reaching_definitions import build_reaching_definitions
from analysis.def_use import build_def_use
from analysis.dependency_graph import build_dependency_graph
from analysis.instruction_cfg import build_instruction_cfg


def analyze(code: str):

    # 1. PARSE
    ir = parse_stl_mvp(code)
    instructions = ir["instructions"]
    
    instruction_cfg = build_instruction_cfg(instructions)
    ir["instruction_cfg"] = instruction_cfg

    # 2. CONTROL FLOW
    blocks = build_basic_blocks(ir)
    cfg = build_block_cfg(blocks, ir)

    ir["blocks"] = blocks
    ir["cfg"] = cfg

    # 3. DATAFLOW

    use_def = build_use_def(instructions)
    ir["use_def"] = use_def

    reaching = build_reaching_definitions(instructions, cfg)
    ir["reaching"] = reaching

    def_use = build_def_use(use_def)
    ir["def_use"] = def_use

    # 4. DEPENDENCY GRAPH
    ir["dep_graph"] = build_dependency_graph(ir)

    return ir