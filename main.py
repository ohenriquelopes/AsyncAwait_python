import time
import asyncio

async def calcular_imposto(faturamento):
    print(faturamento * 0.1)


async def calcular_bonus_funcionarios(vendas):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, "Bonus", venda * 0.05)
        # time.sleep(1)
        await asyncio.sleep(1)
async def fechamento():
    vendas = {
        "Joao": 1000,
        "Maria": 1500,
        "Jose": 1500
    }
    faturamento = 1000
    tarefa1 = asyncio.create_task(calcular_bonus_funcionarios(vendas))
    tarefa2 = asyncio.create_task(calcular_imposto(faturamento))
    print("Finalizou")
    await tarefa1
    await tarefa2

asyncio.run(fechamento())