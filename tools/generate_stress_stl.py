from pathlib import Path

OUT = Path("data/stress_test.awl")
OUT.parent.mkdir(exist_ok=True)

lines = []

for network in range(1, 51):  # ~20 строк на сеть => ~1000 строк
    lines.append("NETWORK")
    lines.append(f"TITLE = Stress Network {network}")
    lines.append("")

    lines.append(f"N{network}_START : NOP 0")
    lines.append('A     "Sensor_1"')
    lines.append('AN    "Fault"')
    lines.append(f"JC    N{network}_STOP")

    lines.append('L     DB10.DBW0')
    lines.append('L     1')
    lines.append('+I')
    lines.append('T     DB10.DBW0')

    lines.append("A(")
    lines.append('A     "Sensor_2"')
    lines.append('O     "Sensor_3"')
    lines.append(")")
    lines.append(f"JC    N{network}_STOP")

    lines.append("CALL FB100")
    lines.append("")

    lines.append(f"N{network}_LOOP : NOP 0")
    lines.append('L     MW100')
    lines.append('L     1')
    lines.append('+I')
    lines.append('T     MW100')
    lines.append(f"JU    N{network}_LOOP")

    lines.append("")
    lines.append(f"N{network}_STOP : R \"MotorEnable\"")
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")

print(f"Generated: {OUT}")
print(f"Lines: {len(lines)}")