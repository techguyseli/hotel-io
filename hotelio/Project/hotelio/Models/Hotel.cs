namespace hotelio.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class Hotel
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public Hotel()
        {
            Chambres = new HashSet<Chambre>();
            Commentaires = new HashSet<Commentaire>();
            Options = new HashSet<Option>();
        }

        [Key]
        public int idHotel { get; set; }

        [Required]
        [StringLength(25)]
        public string nom { get; set; }

        public int nbrEtoiles { get; set; }

        [Required]
        [StringLength(50)]
        public string rib { get; set; }

        public int? idVille { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Chambre> Chambres { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Commentaire> Commentaires { get; set; }

        public virtual Ville Ville { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Option> Options { get; set; }
    }
}
