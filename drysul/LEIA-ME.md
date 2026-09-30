# Drysul — site de demonstração

Proposta de site para a **Drysul — gesso e acabamento**. HTML, CSS e JavaScript puros: sem build e sem dependências. A demonstração é publicada pelo GitHub Pages.

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Página única: hero, categorias, linha Drysul, catálogo, ofertas, calculadora, como funciona, soluções, inspiração, a Drysul, contato |
| `js/data.js` | **Fonte única de dados**: contato, categorias, produtos, preços e ofertas |
| `js/calculator-model.js` | Coeficientes e validação da calculadora (sem DOM, testável no Node) |
| `js/app.js` | Catálogo, busca, filtros, orçamento, WhatsApp, calculadora, menu |
| `js/motion.js` | Canvas técnico, entradas ao rolar, parallax, camadas do hero, ponteiro, pausa de efeitos |
| `css/styles.css` | Design system (tokens, componentes, seções, responsivo) |
| `css/motion.css` | Animações; estados ocultos só existem com efeitos ativos |
| `assets/` | Logo e padrão vetoriais (do arquivo oficial da marca), fotos do manual em WebP, fonte Archivo (OFL) |
| `tests/calculator.test.js` | Casos conferidos com a calculadora de referência |

## Como editar

- **Preço, produto ou oferta:** edite `js/data.js`. `preco: null` mostra "Sob consulta".
- **Foto real de produto:** coloque a imagem em `assets/img/` e preencha `foto: 'assets/img/nome.webp'` no produto. Sem foto, aparece o desenho técnico.
- **Telefone, endereço, Instagram:** objeto `loja` em `js/data.js` (rodapé, contato e WhatsApp leem dali).

## Testes

```bash
node --test drysul/tests/calculator.test.js
```

## Pendências para a versão final

- Fotos originais dos produtos e catálogo completo (preços, marcas, medidas)
- Cidade/CEP, horário de atendimento e área de entrega
- Domínio próprio, remover o `noindex` e a barra "Demo", SEO local (Schema.org LocalBusiness)
