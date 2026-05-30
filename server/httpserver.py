from flask import request, Response, jsonify, render_template

from server import app
from server.models import Region


@app.route('/aistudio')
def portal():
    return render_template('index.html')


# ─── Regions API ────────────────────────────────────────────

@app.route('/api/regions/tree')
def regions_tree():
    """返回完整行政区划树（仅顶级省份，含嵌套 children）"""
    provinces = Region.query.filter(
        Region.level == 'province'
    ).order_by(Region.sort_order).all()
    return jsonify([p.to_dict() for p in provinces])


@app.route('/api/regions/<int:region_id>')
def region_detail(region_id):
    """返回单个地区详情"""
    region = Region.query.get(region_id)
    if region is None:
        return jsonify({'error': 'not found'}), 404
    return jsonify(region.to_dict())
