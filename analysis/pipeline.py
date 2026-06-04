from parser import parse_stl_mvp
from analysis.basic_blocks import build_basic_blocks, build_block_cfg
from analysis.dataflow import build_use_def
from analysis.reaching_definitions import build_reaching_definitions


def analyze(code: str):
    # 1. PARSE
    parsed = parse_stl_mvp(code)
    instructions = parsed["instructions"]

    # 2. CONTROL FLOW
    blocks = build_basic_blocks(parsed)
    block_cfg = build_block_cfg(blocks, parsed)

    # 3. DATAFLOW (USE / DEF)
    use_def = build_use_def(instructions)

    # 4. DATAFLOW (REACHING DEFINITIONS)
    reaching = build_reaching_definitions(parsed["instructions"])

    # 5. RETURN SINGLE STRUCTURE
    return {
        "parsed": parsed,
        "instructions": instructions,

        "blocks": blocks,
        "block_cfg": block_cfg,

        "use_def": use_def,
        "reaching": reaching
    }