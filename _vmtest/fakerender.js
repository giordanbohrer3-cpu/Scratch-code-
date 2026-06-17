// Renderizador "stub": faz o scratch-vm pedir redraw (e portanto ceder 1 vez
// por frame, como no player real), sem precisar de WebGL. Usamos colisão por
// matemática, então não precisamos de pixels — só do contrato de métodos.
module.exports = function fakeRenderer() {
  let id = 1;
  const base = {
    createDrawable: () => id++,
    destroyDrawable: () => {},
    getFencedPositionOfDrawable: (_id, pos) => pos,
    updateDrawableProperties: () => {},
    updateDrawablePosition: () => {},
    updateDrawableDirectionScale: () => {},
    updateDrawableVisible: () => {},
    updateDrawableEffect: () => {},
    updateDrawableSkinId: () => {},
    setDrawableOrder: () => 0,
    getBounds: () => ({ left: -12, right: 12, top: 28, bottom: -28 }),
    getBoundsForBubble: () => ({ left: -12, right: 12, top: 28, bottom: -28 }),
    getCurrentSkinSize: () => [24, 56],
    getSkinSize: () => [24, 56],
    isTouchingDrawables: () => false,
    touchingColor: () => false,
    colorIsTouchingColor: () => false,
    penClear: () => {}, penPoint: () => {}, penLine: () => {}, penStamp: () => {},
    createBitmapSkin: () => id++, createSVGSkin: () => id++, createPenSkin: () => id++,
    createTextSkin: () => id++,
    updateSVGSkin: () => {}, updateBitmapSkin: () => {}, updateTextSkin: () => {},
    destroySkin: () => {}, getSkinRotationCenter: () => [0, 0],
    pick: () => -1, drawableTouching: () => false,
    extractDrawableScreenSpace: () => ({ data: [], width: 0, height: 0 }),
    requestRedraw: () => {},
    setLayerGroupOrdering: () => {},
    draw: () => {}, setStageSize: () => {}, resize: () => {},
    setBackgroundColor: () => {}, _allDrawables: [],
  };
  return new Proxy(base, { get: (t, p) => (p in t ? t[p] : () => {}) });
};
