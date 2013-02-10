class CreatePhotos < ActiveRecord::Migration
  def change
    create_table :photos do |t|
      t.string :description
      t.integer :cube_id
      
      t.timestamps
    end
  end
end
