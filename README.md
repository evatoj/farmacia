# O que está faltando:
1. Corrigir o sistema de compras:
   - O sistema de compras está funcionando, porém ele está decrementando o estoque antes da compra ser confirmada pelo vendedor associado; (CORRIGIDO)
   - Também precisa corrigir o sistema de confirmação de compras de cada vendedor, visto que apenas o vendedor associado à compra deve ter permissão para confirmá-la:
     - No sistema atual, qualquer vendedor está podendo confirmar uma compra, mesmo que não esteja associada ao ID dele.
2. Implementar uma procedure para testar a geração de um relatório (nesse caso, apenas o gerente será responsável por emitir um relatório de vendas de um determinado vendedor);
3. Ver onde é possível encaixar um **trigger** no sistema;
4. Fazer uma interface gráfica simples, mas isso só será tratado após as prioridades acima serem concluídas.
